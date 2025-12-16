# Release notes

<!-- do not remove -->

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

