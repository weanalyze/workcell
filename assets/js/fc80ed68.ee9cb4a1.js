"use strict";(self.webpackChunkworkcell_doc=self.webpackChunkworkcell_doc||[]).push([[8477],{3905:(e,t,n)=>{n.d(t,{Zo:()=>u,kt:()=>g});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function p(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var s=r.createContext({}),l=function(e){var t=r.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},u=function(e){var t=l(e.components);return r.createElement(s.Provider,{value:t},e.children)},c="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,s=e.parentName,u=p(e,["components","mdxType","originalType","parentName"]),c=l(n),d=a,g=c["".concat(s,".").concat(d)]||c[d]||m[d]||o;return n?r.createElement(g,i(i({ref:t},u),{},{components:n})):r.createElement(g,i({ref:t},u))}));function g(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=d;var p={};for(var s in t)hasOwnProperty.call(t,s)&&(p[s]=t[s]);p.originalType=e,p[c]="string"==typeof e?e:a,i[1]=p;for(var l=2;l<o;l++)i[l]=n[l];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},9902:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>m,frontMatter:()=>o,metadata:()=>p,toc:()=>l});var r=n(7462),a=(n(7294),n(3905));const o={sidebar_position:3},i="Read pilot",p={unversionedId:"tutorials/read-pilot",id:"tutorials/read-pilot",title:"Read pilot",description:"Learn how to use workcell to integate with OpenAI API.",source:"@site/docs/tutorials/read-pilot.md",sourceDirName:"tutorials",slug:"/tutorials/read-pilot",permalink:"/workcell/docs/tutorials/read-pilot",draft:!1,editUrl:"https://github.com/weanalyze/workcell/edit/main/docs/tutorials/read-pilot.md",tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"tutorialSidebar",previous:{title:"Model serving",permalink:"/workcell/docs/tutorials/model-serving"},next:{title:"Documents",permalink:"/workcell/docs/category/documents"}},s={},l=[{value:"Motivation",id:"motivation",level:2},{value:"Code",id:"code",level:2},{value:"Step-by-step implementation",id:"step-by-step-implementation",level:2},{value:"Step1. Prepare an OpenAI API key",id:"step1-prepare-an-openai-api-key",level:3},{value:"Step2. Install dependencies",id:"step2-install-dependencies",level:3},{value:"Step3. Implement a webpage extractor",id:"step3-implement-a-webpage-extractor",level:3},{value:"Step4. Implement a content summarizer",id:"step4-implement-a-content-summarizer",level:3},{value:"Step5. Create a workcell",id:"step5-create-a-workcell",level:3},{value:"Step6. Serving or deploying",id:"step6-serving-or-deploying",level:3}],u={toc:l},c="wrapper";function m(e){let{components:t,...n}=e;return(0,a.kt)(c,(0,r.Z)({},u,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"read-pilot"},"Read pilot"),(0,a.kt)("p",null,"Learn how to use workcell to integate with OpenAI API."),(0,a.kt)("h2",{id:"motivation"},"Motivation"),(0,a.kt)("p",null,(0,a.kt)("a",{parentName:"p",href:"https://openai.com/"},"OpenAI"),"'s GPT-3 (Generative Pre-trained Transformer 3) is a state-of-the-art language model that can generate natural language text in response to input prompts. The GPT-3 API allows developers and researchers to access this powerful language model using simple API requests, enabling them to build a wide range of applications such as chatbots, language translation systems, content generators, and more."),(0,a.kt)("p",null,"In this tutorial, we will built an AI-powered read pilot that generates thought-provoking discussion questions from webpage content using OpenAI GPT-3 API."),(0,a.kt)("admonition",{type:"note"},(0,a.kt)("p",{parentName:"admonition"},"You need an ",(0,a.kt)("a",{parentName:"p",href:"http://beta.openai.com/"},"OpenAI API Key")," to deploy this app.")),(0,a.kt)("h2",{id:"code"},"Code"),(0,a.kt)("p",null,"The source code of this tutorial is on ",(0,a.kt)("a",{parentName:"p",href:"https://huggingface.co/spaces/jiandong/analyze_url"},"Hugging Face Spaces"),"."),(0,a.kt)("p",null,"The project dir as follows:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-console"},"\u279c tree -L 2 ./              \n./\n\u251c\u2500\u2500 app.py\n\u251c\u2500\u2500 requirements.txt\n\u2514\u2500\u2500 utils\n    \u251c\u2500\u2500 extractor.py\n    \u2514\u2500\u2500 summarizer.py\n\n2 directories, 4 files\n")),(0,a.kt)("h2",{id:"step-by-step-implementation"},"Step-by-step implementation"),(0,a.kt)("h3",{id:"step1-prepare-an-openai-api-key"},"Step1. Prepare an OpenAI API key"),(0,a.kt)("p",null,"Set up an OpenAI API account and obtain an API key."),(0,a.kt)("h3",{id:"step2-install-dependencies"},"Step2. Install dependencies"),(0,a.kt)("p",null,"Install the openai Python library using pip."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-console"},"pip install openai\n")),(0,a.kt)("h3",{id:"step3-implement-a-webpage-extractor"},"Step3. Implement a webpage extractor"),(0,a.kt)("p",null,"Define a function that extracts the text content from the webpage using a Python library such as ",(0,a.kt)("a",{parentName:"p",href:"https://github.com/rushter/selectolax"},"selectolax"),"."),(0,a.kt)("details",null,(0,a.kt)("summary",null,"Python file to extract webpage"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="{project_folder}/utils/extractor.py"',title:'"{project_folder}/utils/extractor.py"'},"import requests\nfrom selectolax.parser import HTMLParser\nimport re\nfrom string import punctuation\n\n\ndef preprocess_text(text):\n    text = text.lower()  # Lowercase text\n    # punctuation = r'\\'\\\":'\n    text = re.sub(f\"[{re.escape(punctuation)}]\", \"\", text)  # Remove punctuation\n    text = \" \".join(text.split())  # Remove extra spaces, tabs, and new lines\n    return text\n\ndef get_html(url):\n    # request web page\n    resp = requests.get(url)\n    # get the response text. in this case it is HTML\n    html = resp.text\n    return html\n\ndef get_text(html):\n    tree = HTMLParser(html)\n    if tree.body is None:\n        return None\n    for tag in tree.css('script'):\n        tag.decompose()\n    for tag in tree.css('style'):\n        tag.decompose()\n    # get the text from the body tag\n    text = tree.body.text(separator='')\n    # preprocess\n    text = preprocess_text(text)\n    return text\n\ndef get_html_text(url):\n    html = get_html(url)\n    text = get_text(html)\n    return text\n"))),(0,a.kt)("h3",{id:"step4-implement-a-content-summarizer"},"Step4. Implement a content summarizer"),(0,a.kt)("p",null,"Define a function that uses the OpenAI client to generate discussion questions based on the extracted text. "),(0,a.kt)("p",null,"You may need to apply some prompt engineering techniques to ensure that the generated questions are relevant and thought-provoking."),(0,a.kt)("admonition",{title:"what-is-prompt-engineering?",type:"tip"},(0,a.kt)("p",{parentName:"admonition"},'For example, you could use the extracted text as input to the OpenAI API and add a prefix such as "What might be some interesting discussion questions related to this passage?" or "What implications does this passage have for society?" to guide the model towards generating relevant questions. Further reading: ',(0,a.kt)("a",{parentName:"p",href:"https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api"},"best-practices-for-prompt-engineering-with-openai-api"))),(0,a.kt)("details",null,(0,a.kt)("summary",null,"Python file to summarize webpage"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="{project_folder}/utils/summarizer.py"',title:'"{project_folder}/utils/summarizer.py"'},'import ast\nimport openai\nfrom transformers import GPT2Tokenizer\n\n# Initialize tokenizer\ntokenizer = GPT2Tokenizer.from_pretrained("gpt2")\n\n# Prompt engineering\ndef get_prompt(text):\n    prompt_prefix = """Generate exactly 3 different and thought provoking discussion questions about given article below, and return the answers of these questions with the evidence.\n    \n    Desired output format: [{"Q":<question>,"A":<answer>},{"Q":<question>,"A":<answer>},{"Q":<question>,"A":<answer>}].\n    """ \n    prompt_postfix ="""\n    Given article content: \\"""{}.\\"""\n    """\n    prompt = prompt_prefix + prompt_postfix.format(text)\n    return prompt\n\ndef limit_tokens(text, n=3000):\n    # Get the first n tokens from the input text\n    input_ids = tokenizer.encode(text, return_tensors="pt")\n    first_n_tokens = input_ids[:, :n]\n    # Convert the first n tokens back to text format\n    processed_text = tokenizer.decode(first_n_tokens[0], skip_special_tokens=True)    \n    return processed_text\n\ndef get_openai_completion(text):\n    processed_text = limit_tokens(text)\n    augmented_prompt = get_prompt(processed_text)\n\n    try:\n        result = openai.Completion.create(\n            model="text-davinci-003",\n            prompt=augmented_prompt,\n            temperature=0.7,\n            top_p=1,\n            frequency_penalty=0,\n            presence_penalty=0,\n            max_tokens=500,\n            stream=False, \n            n=1\n        )\n    except:\n        raise\n    return result\n\ndef get_analyze(result):\n    try:\n        # analyze = ast.literal_eval(result["choices"][0][\'text\'])\n        analyze = eval(result["choices"][0][\'text\'])\n    except:\n        raise    \n    return analyze\n\ndef get_analyze_result(text):\n    result = get_openai_completion(text)\n    analyze = get_analyze(result)\n    return analyze\n'))),(0,a.kt)("h3",{id:"step5-create-a-workcell"},"Step5. Create a workcell"),(0,a.kt)("p",null,"Create a workcell web application that accepts a URL as input and returns a list of result generated by GPT-3."),(0,a.kt)("details",null,(0,a.kt)("summary",null,"Python file to create workcell"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python",metastring:'title="{project_folder}/app.py"',title:'"{project_folder}/app.py"'},'import os\nfrom typing import Dict, List\nfrom pydantic import BaseModel, Field\n\nimport openai\nfrom utils.summarizer import get_analyze_result\nfrom utils.extractor import get_html_text\n\n\nclass Input(BaseModel):\n    url: str\n\nclass Output(BaseModel):\n    analyze: List[Dict[str, str]] = Field(\n        ..., description="A lisf of dict Q&A response, generated by OpenAI GPT3."\n    )\n\ndef analyze_url(input: Input) -> Output:\n    """Returns a thought provoking discussion questions from url provided, generated by OpenAI GPT3 API."""\n    openai.api_key = os.getenv(\'SECRET_OPENAI_API_KEY\')\n    # return summarization\n    text = get_html_text(input.url)\n    analyze = get_analyze_result(text)\n    output = Output(\n        analyze=analyze\n    )\n    return output\n'))),(0,a.kt)("h3",{id:"step6-serving-or-deploying"},"Step6. Serving or deploying"),(0,a.kt)("p",null,"That's it! With these steps, you will have built an AI-powered read pilot that generates thought-provoking discussion questions from webpage content using OpenAI GPT-3 API."))}m.isMDXComponent=!0}}]);