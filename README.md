# Open-source apps that call Google's Custom Search JSON API (ends January 1, 2027)

On November 11, 2026, 51 days before the end, 16 of 16 projects in this list still hold Google's address on their default branch. None has merged a change that moves the call. Together they have 649,530 GitHub stars.

Google's [Custom Search JSON API overview](https://developers.google.com/custom-search/v1/overview) says: "Existing Custom Search JSON API customers have until January 1, 2027 to transition to an alternative solution." Its pricing applies "until the service discontinuation on January 1, 2027." The API is already closed to new customers, so a new user of these projects cannot get a Google key today.

## The 16 projects

Most starred first. Stars are GitHub's count on November 11, 2026. Each file link opens the default branch at the line that holds the address. "Setting" means a self-hoster can point the project at another address without editing code. "Code" means the address is in the line named.

| Project | Stars | File and line | Setting or code | In public about the ending | Guide |
|---|---|---|---|---|---|
| [Open WebUI](https://github.com/open-webui/open-webui) | 158,326 | [`backend/open_webui/retrieval/web/google_pse.py` line 24](https://github.com/open-webui/open-webui/blob/main/backend/open_webui/retrieval/web/google_pse.py#L24) | Code: one line | [#20961](https://github.com/open-webui/open-webui/issues/20961) (closed issue), [#8124](https://github.com/open-webui/open-webui/issues/8124) (closed issue) | [https://specstream.ai/google-pse/open-webui](https://specstream.ai/google-pse/open-webui) |
| [OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 86,301 | [`src/lib/providers/validation/searchProviders.ts` line 119](https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.54/src/lib/providers/validation/searchProviders.ts#L119) | Code: one line | [#1984](https://github.com/cheaper-inference/OmniRoute/issues/1984) (closed issue) |  |
| [LobeHub](https://github.com/lobehub/lobehub) | 84,873 | [`apps/server/src/services/search/impls/google/index.ts` line 37](https://github.com/lobehub/lobehub/blob/canary/apps/server/src/services/search/impls/google/index.ts#L37) | Code: one line | [#19801](https://github.com/lobehub/lobehub/pull/19801) (open pull request that adds another paid provider beside Google) | [https://specstream.ai/web-search/lobehub](https://specstream.ai/web-search/lobehub) |
| [LiteLLM](https://github.com/BerriAI/litellm) | 63,067 | [`litellm/llms/google_pse/search/transformation.py` line 64](https://github.com/BerriAI/litellm/blob/main/litellm/llms/google_pse/search/transformation.py#L64) | Setting: env `GOOGLE_PSE_API_BASE` | nothing found | [https://specstream.ai/google-pse/litellm](https://specstream.ai/google-pse/litellm) |
| [AutoGen](https://github.com/microsoft/autogen) | 61,778 | [`python/packages/autogen-studio/autogenstudio/gallery/tools/google_search.py` line 103](https://github.com/microsoft/autogen/blob/main/python/packages/autogen-studio/autogenstudio/gallery/tools/google_search.py#L103) | Code: one line | nothing found |  |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 52,869 | [`llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/search/base.py` line 11](https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/tools/llama-index-tools-google/llama_index/tools/google/search/base.py#L11) | Code: one line | nothing found |  |
| [Discourse AI](https://github.com/discourse/discourse) | 48,074 | [`plugins/discourse-ai/lib/agents/tools/google.rb` line 47](https://github.com/discourse/discourse/blob/main/plugins/discourse-ai/lib/agents/tools/google.rb#L47) | Code: one line | [#45934](https://github.com/discourse/discourse/pull/45934) (open pull request by SpecStream that makes the endpoint a site setting) |  |
| [Khoj](https://github.com/khoj-ai/khoj) | 38,104 | [`src/khoj/processor/tools/online_search.py` line 362](https://github.com/khoj-ai/khoj/blob/master/src/khoj/processor/tools/online_search.py#L362) | Code: one line | nothing found | [https://specstream.ai/web-search/khoj](https://specstream.ai/web-search/khoj) |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | 30,621 | [`gpt_researcher/retrievers/google/google.py` line 79](https://github.com/assafelovic/gpt-researcher/blob/main/gpt_researcher/retrievers/google/google.py#L79) | Code: one line | nothing found | [https://specstream.ai/google-pse/gpt-researcher](https://specstream.ai/google-pse/gpt-researcher) |
| [Marvin](https://github.com/PrefectHQ/marvin) | 6,204 | [`examples/deepseek_chat.py` line 55](https://github.com/PrefectHQ/marvin/blob/main/examples/deepseek_chat.py#L55) | Code: one line | nothing found |  |
| [ScriptCat](https://github.com/scriptscat/scriptcat) | 5,846 | [`src/app/service/agent/core/tools/web_search.ts` line 145](https://github.com/scriptscat/scriptcat/blob/main/src/app/service/agent/core/tools/web_search.ts#L145) | Code: one line | nothing found |  |
| [OpenAgent](https://github.com/the-open-agent/openagent) | 5,742 | [`tool/web_search.go` line 113](https://github.com/the-open-agent/openagent/blob/master/tool/web_search.go#L113) | Setting: config field `ProviderUrl` | nothing found | [https://specstream.ai/google-pse/openagent](https://specstream.ai/google-pse/openagent) |
| [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL) | 4,176 | [`openmanus_rl/tools/google_search/tool.py` line 54](https://github.com/OpenManus/OpenManus-RL/blob/main/openmanus_rl/tools/google_search/tool.py#L54) | Code: one line | nothing found |  |
| [Swirl](https://github.com/swirlai/swirl-search) | 3,049 | [`docs/SP-Guide.md` line 228](https://github.com/swirlai/swirl-search/blob/main/docs/SP-Guide.md#L228) | Setting: `url` in the SearchProvider JSON | nothing found | [https://specstream.ai/google-pse/swirl](https://specstream.ai/google-pse/swirl) |
| [Mattermost Agents](https://github.com/mattermost/mattermost-plugin-agents) | 257 | [`websearch/google.go` line 19](https://github.com/mattermost/mattermost-plugin-agents/blob/master/websearch/google.go#L19) | Setting: System Console field "API URL (optional)" | [#1058](https://github.com/mattermost/mattermost-plugin-agents/pull/1058) (open pull request that adds another paid provider beside Google) | [https://specstream.ai/google-pse/mattermost-agents](https://specstream.ai/google-pse/mattermost-agents) |
| [aimux](https://github.com/arcships/aimux) | 243 | [`aimux-providers/src/google_pse.rs` line 60](https://github.com/arcships/aimux/blob/master/aimux-providers/src/google_pse.rs#L60) | Setting: provider setting `baseUrl` | nothing found | [https://specstream.ai/google-pse/aimux](https://specstream.ai/google-pse/aimux) |

4 of the 16 have an issue or pull request about the ending opened by someone other than SpecStream: Open WebUI, OmniRoute, LobeHub and Mattermost Agents. [discourse/discourse#45934](https://github.com/discourse/discourse/pull/45934) is ours.

## Check it yourself

```
python3 check.py
```

It needs Python 3 and nothing else: no packages and no GitHub token. For each project in `projects.json` it fetches the file from `raw.githubusercontent.com` at the default branch and prints one of four results: `still there at line N`, `moved to line N`, `gone from the file` or `file not found`. The last line counts the projects that still hold Google's address and gives the date. It changes nothing.

Output of the run on November 11, 2026 at 01:07 UTC:

```
open-webui/open-webui                still there at line 24
cheaper-inference/OmniRoute          still there at line 119
lobehub/lobehub                      still there at line 37
BerriAI/litellm                      still there at line 64
microsoft/autogen                    still there at line 103
run-llama/llama_index                still there at line 11
discourse/discourse                  still there at line 47
khoj-ai/khoj                         still there at line 362
assafelovic/gpt-researcher           still there at line 79
PrefectHQ/marvin                     still there at line 55
scriptscat/scriptcat                 still there at line 145
the-open-agent/openagent             still there at line 113
OpenManus/OpenManus-RL               still there at line 54
swirlai/swirl-search                 still there at line 228
mattermost/mattermost-plugin-agents  still there at line 19
arcships/aimux                       still there at line 60

16 of 16 projects still hold Google's address. Checked 2026-11-11 (UTC).
```

## The change

5 projects read Google's address from a setting: LiteLLM (`GOOGLE_PSE_API_BASE`), OpenAgent (`ProviderUrl`), Swirl (`url` in the SearchProvider JSON), Mattermost Agents ("API URL (optional)") and aimux (`baseUrl`). A self-hoster sets it to `https://api.specstream.ai/customsearch/v1` and puts a SpecStream key where the Google key goes. For LiteLLM:

```
export GOOGLE_PSE_API_BASE=https://api.specstream.ai/customsearch/v1
export GOOGLE_PSE_API_KEY=$SPECSTREAM_KEY
# keep GOOGLE_PSE_ENGINE_ID as it is; cx is accepted and not used
```

The other 11 hold `https://www.googleapis.com` in the line the table names. The change is that one line: `https://www.googleapis.com` becomes `https://api.specstream.ai`. A maintainer can also read the address from a setting, so each self-hoster chooses it. Either change reaches every user with the next release.

```
# Before
curl "https://www.googleapis.com/customsearch/v1?key=$GOOGLE_KEY&cx=$CX&q=open+source+vector+databases"

# After
curl "https://api.specstream.ai/customsearch/v1?key=$SPECSTREAM_KEY&cx=$CX&q=open+source+vector+databases"
```

The path, the parameters and the parser stay the same. The reply has `kind` `customsearch#search`, `items[]` with `title`, `link`, `snippet` and `displayLink`, `searchInformation.totalResults` and `queries.nextPage`. The route honors nine parameters: `q`, `num`, `start`, `hq`, `exactTerms`, `orTerms`, `excludeTerms`, `siteSearch` and `siteSearchFilter`. `cx` is accepted and not used. The key goes in `key=`, in the `X-Goog-Api-Key` header or as a Bearer token.

## Add or correct a project

Open an issue, or a pull request that edits `projects.json`, with the repository, the file path, the line and the default branch. We read the file at that line again before we merge. If a project has moved its call, a pull request that updates its row and its public items is welcome too.

## Method

On November 10, 2026, GitHub code search found 25,024 public files that contain `googleapis.com/customsearch/v1`. That day we read 74 open-source projects at their source and checked 28 at their latest commit. 16 of them are AI apps whose code calls the API, and those are the rows here.

On November 11, 2026 we read each repository's stars and default branch, fetched the file on that branch, and searched its issues and pull requests on six phrases: `"custom search" 2027`, `"customsearch" deprecated`, `"Custom Search JSON API"`, `"PSE" discontinued`, `"google pse" shutdown` and `"programmable search" deprecated`. We kept the items about the ending and dropped unrelated hits. Discussions were not searched, and an item the GitHub search index does not return is not in the list.

## Who keeps this

[SpecStream](https://specstream.ai), the live web data engine. Its Search API answers the Custom Search JSON API's calls on the same path and in the same JSON, at $5 per 1,000 searches. New accounts get $10 of credit with no card.

1. [Migration guide for the Custom Search JSON API](https://specstream.ai/migrate/google-custom-search)
2. [The 16 apps, with the line in each](https://specstream.ai/google-custom-search-api-open-source-apps)
3. [The blog post on the end of the API and these apps](https://specstream.ai/blog/google-custom-search-api-ends-open-source-apps)

## License

`check.py` is under the MIT license in [LICENSE](LICENSE). The data in `projects.json` and `projects.csv` is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit "SpecStream".
