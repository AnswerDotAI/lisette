import json,asyncio
from litellm import acompletion, ModelResponse, stream_chunk_builder
from toolslm.funccall import call_func_async
from fastcore.utils import *
from lisette.core import *
async def _alite_call_func(tc, ns, raise_on_err=True):
    res = await call_func_async(tc.function.name, json.loads(tc.function.arguments), ns=ns)
    return {"tool_call_id": tc.id, "role": "tool", "name": tc.function.name, "content": str(res)}
@asave_iter
async def astream_result(self, agen, postproc=noop):
    chunks = []
    async for chunk in agen:
        chunks.append(chunk)
        yield chunk
    postproc(chunks)
    self.value = stream_chunk_builder(chunks)
class AsyncChat(Chat):
    async def _call(self, msg=None, stream=False, max_tool_rounds=1, tool_round=0, final_prompt=None, tool_choice=None, **kwargs):
        "Internal method that always yields responses"
        msgs = self._prepare_msgs(msg)
        res = await acompletion(model=self.model, messages=msgs, stream=stream,
                         tools=self.tool_schemas, temperature=self.temp, **kwargs)
        if stream:
            res = astream_result(res, postproc=cite_footnotes)
            async for chunk in res: yield chunk
            res = res.value
        
        yield res
        m = res.choices[0].message
        self.hist.append(m)

        if tcs := m.tool_calls:
            tool_results = [await _alite_call_func(tc, ns=self.ns) for tc in tcs]
            if tool_round>=max_tool_rounds-1:
                tool_results += ([{"role": "user", "content": final_prompt}] if final_prompt else [])
                tool_choice='none'
            async for result in self._call(
                tool_results, stream, max_tool_rounds, tool_round+1,
                final_prompt, tool_choice=tool_choice, **kwargs):
                    yield result
    
    async def __call__(self, msg=None, stream=False, max_tool_rounds=1, final_prompt=None, return_all=False, **kwargs):
        "Main call method - handles streaming vs non-streaming"
        if stream: return self._call(msg, stream, max_tool_rounds, 0, final_prompt, **kwargs)
        result_gen = self._call(msg, stream, max_tool_rounds, 0, final_prompt, **kwargs)
        if return_all: return [result async for result in result_gen] # toolloop behavior
        else: return [result async for result in result_gen][-1]      # normal chat behavior