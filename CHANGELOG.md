# Release notes

<!-- do not remove -->

## 0.1.21

### New Features

- Support kimi fireworks vision ([#152](https://github.com/AnswerDotAI/lisette/issues/152))


## 0.1.20

### New Features

- Add `CodexChat` ([#150](https://github.com/AnswerDotAI/lisette/issues/150))


## 0.1.19

### New Features

- kimi-k2p6 ([#149](https://github.com/AnswerDotAI/lisette/issues/149))



## 0.1.17

### New Features

- Workaround for https://github.com/BerriAI/litellm/issues/26153 ([#148](https://github.com/AnswerDotAI/lisette/issues/148))


## 0.1.15

### New Features

- Anthropic max thinking support ([#147](https://github.com/AnswerDotAI/lisette/issues/147))


## 0.1.13

### New Features

- Add `tool_reminder` param to Chat for transient reminder injection ([#146](https://github.com/AnswerDotAI/lisette/issues/146))
- Add GPT-5.4 model support and xhigh thinking effort for opus-4-7 ([#145](https://github.com/AnswerDotAI/lisette/issues/145))


## 0.1.11

### New Features

- Support opus 4.7, anthropic adaptive thinking, and work around gemini litellm bugs ([#144](https://github.com/AnswerDotAI/lisette/issues/144))


## 0.1.10

- Sonnet 4.6 included


## 0.1.9

### New Features

- Add FireworksAI reasoning support for Kimi models and fix stream usage tracking ([#143](https://github.com/AnswerDotAI/lisette/issues/143))


## 0.1.8

### New Features

- Do not truncate `Safe` strs ([#142](https://github.com/AnswerDotAI/lisette/issues/142))


## 0.1.5

### New Features

- Disable anthropic beta web search ([#141](https://github.com/AnswerDotAI/lisette/issues/141))


## 0.1.4

### New Features

- Export `status_re` and add named capture in `re_tools` ([#140](https://github.com/AnswerDotAI/lisette/issues/140))


## 0.1.3

### New Features

- Optionally preserve full content in tool result details ([#139](https://github.com/AnswerDotAI/lisette/issues/139))


## 0.1.2

### New Features

- Use code block and `escape` for tool summaries and previews ([#138](https://github.com/AnswerDotAI/lisette/issues/138))


## 0.1.1

### New Features

- Add skip/replace params to `_trunc_str`, show tool results in `_tc_summary` ([#137](https://github.com/AnswerDotAI/lisette/issues/137))


## 0.1.0

### New Features

- Refactor usage tracking: replace `fmt_usage`/Usage with UsageStats class, add Chat.use accumulator and markup support, move `search_count` to core ([#136](https://github.com/AnswerDotAI/lisette/issues/136))


## 0.0.49

### New Features

- Show pending tool call indicators in StreamFormatter ([#135](https://github.com/AnswerDotAI/lisette/issues/135))


## 0.0.48

### New Features

- Add StopResponse/FullResponse types and `_has_stop` to allow tools to halt the tool loop early ([#134](https://github.com/AnswerDotAI/lisette/issues/134))


## 0.0.47

### New Features

- Patch AnthropicConfig.`map_web_search_tool` to use `web_search_20260209` type ([#133](https://github.com/AnswerDotAI/lisette/issues/133))


## 0.0.46

### Bugs Squashed

- Pass kwargs to AsyncStreamFormatter init instead of `format_stream` ([#132](https://github.com/AnswerDotAI/lisette/issues/132))


## 0.0.45

### New Features

- Add `pause` param to `AsyncChat` call ([#131](https://github.com/AnswerDotAI/lisette/issues/131))


## 0.0.44

### New Features

- Add litellm workaround to preserve original content blocks for web search + thinking ([#130](https://github.com/AnswerDotAI/lisette/issues/130))


## 0.0.43

### Bugs Squashed

- fix `pause_turn` retry logic and re-enable `pause_turn` tests ([#129](https://github.com/AnswerDotAI/lisette/issues/129))


## 0.0.42

### New Features

- Increase max before trunc for input ([#126](https://github.com/AnswerDotAI/lisette/issues/126))


## 0.0.41

### Bugs Squashed

- Fix `srvtoolu_` id handling, cache index mutation, and retry history ordering ([#125](https://github.com/AnswerDotAI/lisette/issues/125))


## 0.0.40

### New Features

- Limit opus max tokens ([#124](https://github.com/AnswerDotAI/lisette/issues/124))


## 0.0.39

### New Features

- Refactor tool calling: extract shared `_call_func` helper, add tcdict property, use `parallel_async`, and add `num_retries` ([#123](https://github.com/AnswerDotAI/lisette/issues/123))


## 0.0.38

### New Features

- Add Sonnet 4.6 ([#120](https://github.com/AnswerDotAI/lisette/issues/120))


## 0.0.37

### New Features

- Update to latest litellm ([#119](https://github.com/AnswerDotAI/lisette/issues/119))
- Return tool errors to LLM ([#118](https://github.com/AnswerDotAI/lisette/issues/118))
- make parallel tool calls parallel ([#112](https://github.com/AnswerDotAI/lisette/issues/112))

### Bugs Squashed

- Fix `ToolResponse` content being stringified when `tc_res` is `None` ([#116](https://github.com/AnswerDotAI/lisette/pull/116)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.36

### Bugs Squashed

- Refactor `_prep_call`, add `mk_stream_chunk` helper, fix `max_steps` loop logic, add empty choices guards ([#110](https://github.com/AnswerDotAI/lisette/issues/110))


## 0.0.35

### New Features

- Optionally `eval` string reprs when `tc_res=True` ([#105](https://github.com/AnswerDotAI/lisette/pull/105)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)

### Bugs Squashed

- fix cache control in tool calls ([#107](https://github.com/AnswerDotAI/lisette/pull/107)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)
- Add `_try_eval` to convert kernel string reprs (e.g., `"'hello'"`) back to Python objects before storing in `tc_res` for tool call chaining. ([#104](https://github.com/AnswerDotAI/lisette/issues/104))
- Fix AsyncChat to handle unmapped models (fixes #42) ([#100](https://github.com/AnswerDotAI/lisette/pull/100)), thanks to [@PiotrCzapla](https://github.com/PiotrCzapla)


## 0.0.34

### Bugs Squashed

- fix cache miss in tloop ([#103](https://github.com/AnswerDotAI/lisette/pull/103)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.33

### New Features

- Tool call ids and results referencing ([#97](https://github.com/AnswerDotAI/lisette/pull/97)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.31

### New Features

- fix fm2thist and better usage display ([#94](https://github.com/AnswerDotAI/lisette/pull/94)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)
- Improve `final_prompt` to clarify tool access limit is per-turn only ([#88](https://github.com/AnswerDotAI/lisette/pull/88)), thanks to [@benreeve1984](https://github.com/benreeve1984)


## 0.0.30

### Bugs Squashed

- handle length,refusal,pause stop reasons ([#91](https://github.com/AnswerDotAI/lisette/pull/91)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.29

### New Features

- Add `extra_headers` parameter to Chat ([#86](https://github.com/AnswerDotAI/lisette/pull/86)), thanks to [@benreeve1984](https://github.com/benreeve1984)
  - Use case: Corporate API gateways and proxies can require custom authentication headers (e.g., api-key) rather than standard Bearer token auth
- display generated imgs ([#84](https://github.com/AnswerDotAI/lisette/pull/84)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)

### Bugs Squashed

- Upgrade litellm to `>1.80.5` ([#64](https://github.com/AnswerDotAI/lisette/issues/64))
  - There is a web search requests usage related fix in beyond this release.


## 0.0.28

### New Features

- Add `StreamFormatter` ([#83](https://github.com/AnswerDotAI/lisette/issues/83))


## 0.0.27

### Bugs Squashed

- Missing json prefix ([#82](https://github.com/AnswerDotAI/lisette/issues/82))


## 0.0.26

### New Features

- Add tool params to summary ([#81](https://github.com/AnswerDotAI/lisette/issues/81))
- add tc name in details ([#80](https://github.com/AnswerDotAI/lisette/pull/80)), thanks to [@ncoop57](https://github.com/ncoop57)


## 0.0.25

### Bugs Squashed

- fix native tool schemas in func call ([#78](https://github.com/AnswerDotAI/lisette/pull/78)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.24

### Bugs Squashed

- fix import error ([#76](https://github.com/AnswerDotAI/lisette/pull/76)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)


## 0.0.23

### New Features

- Add debug flag to AsyncStreamFormatter ([#75](https://github.com/AnswerDotAI/lisette/issues/75))


## 0.0.22

### New Features

- Check tool in schemas ([#74](https://github.com/AnswerDotAI/lisette/pull/74)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)
- Seeded tool ids for cachy ([#73](https://github.com/AnswerDotAI/lisette/pull/73)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)
- Add CI ([#71](https://github.com/AnswerDotAI/lisette/pull/71)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.21

### New Features

- update litellm 1.80.10 ([#69](https://github.com/AnswerDotAI/lisette/pull/69)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.20

### New Features

- Automatically handle context length issues in tool loop ([#68](https://github.com/AnswerDotAI/lisette/issues/68))
- Gemini multimodal support ([#53](https://github.com/AnswerDotAI/lisette/pull/53)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.19

### New Features

- Truncate long final tool tokens ([#67](https://github.com/AnswerDotAI/lisette/issues/67))


## 0.0.18


### Bugs Squashed

- Fix missing usage import ([#63](https://github.com/AnswerDotAI/lisette/pull/63)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.17

### Bugs Squashed

- Patch not defined in usage.py ([#61](https://github.com/AnswerDotAI/lisette/issues/61))


## 0.0.16

### New Features

- Opus 4.5 ([#56](https://github.com/AnswerDotAI/lisette/issues/56))


## 0.0.15

### New Features

- added contents helper ([#51](https://github.com/AnswerDotAI/lisette/pull/51)), thanks to [@bitcloud2](https://github.com/bitcloud2)

### Bugs Squashed

- hotfix for streaming claude search error ([#54](https://github.com/AnswerDotAI/lisette/pull/54)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)


## 0.0.14

### New Features

- add sqlite usage and cost monitoring ([#47](https://github.com/AnswerDotAI/lisette/pull/47)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.13

### New Features

- support toolcalls to return toolresponses ([#44](https://github.com/AnswerDotAI/lisette/pull/44)), thanks to [@ncoop57](https://github.com/ncoop57)


## 0.0.12

### New Features

- Custom anthropic `cache_idxs` ([#36](https://github.com/AnswerDotAI/lisette/pull/36)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)

### Bugs Squashed

- Toolloop: `A maximum of 4 blocks with cache_control may be provided. Found 5.` ([#34](https://github.com/AnswerDotAI/lisette/issues/34))


## 0.0.11

### Bugs Squashed

- Tool call serialization fails if no final text ([#33](https://github.com/AnswerDotAI/lisette/issues/33))


## 0.0.10

### New Features

- reconstruct tool calls ([#30](https://github.com/AnswerDotAI/lisette/pull/30)), thanks to [@comhar](https://github.com/comhar)


## 0.0.7

### New Features

- make tool call ids deterministic ([#27](https://github.com/AnswerDotAI/lisette/pull/27)), thanks to [@comhar](https://github.com/comhar)


## 0.0.6

### New Features

- Add pdf support ([#25](https://github.com/AnswerDotAI/lisette/pull/25)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)


## 0.0.5

### Bugs Squashed

- Fix cache control ([#23](https://github.com/AnswerDotAI/lisette/pull/23)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)


## 0.0.4

### New Features

- Add Sonnet 4.5 ([#21](https://github.com/AnswerDotAI/lisette/issues/21))


## 0.0.3

### Bugs Squashed

- Need to pin to older litellm for now ([#17](https://github.com/AnswerDotAI/lisette/issues/17))


## 0.0.2

- param updates


## 0.0.1

- init release

