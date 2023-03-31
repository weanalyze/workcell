"use strict";(self.webpackChunkworkcell_doc=self.webpackChunkworkcell_doc||[]).push([[2259],{3905:(e,t,l)=>{l.d(t,{Zo:()=>u,kt:()=>m});var n=l(7294);function r(e,t,l){return t in e?Object.defineProperty(e,t,{value:l,enumerable:!0,configurable:!0,writable:!0}):e[t]=l,e}function a(e,t){var l=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),l.push.apply(l,n)}return l}function o(e){for(var t=1;t<arguments.length;t++){var l=null!=arguments[t]?arguments[t]:{};t%2?a(Object(l),!0).forEach((function(t){r(e,t,l[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(l)):a(Object(l)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(l,t))}))}return e}function i(e,t){if(null==e)return{};var l,n,r=function(e,t){if(null==e)return{};var l,n,r={},a=Object.keys(e);for(n=0;n<a.length;n++)l=a[n],t.indexOf(l)>=0||(r[l]=e[l]);return r}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)l=a[n],t.indexOf(l)>=0||Object.prototype.propertyIsEnumerable.call(e,l)&&(r[l]=e[l])}return r}var p=n.createContext({}),k=function(e){var t=n.useContext(p),l=t;return e&&(l="function"==typeof e?e(t):o(o({},t),e)),l},u=function(e){var t=k(e.components);return n.createElement(p.Provider,{value:t},e.children)},c="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},s=n.forwardRef((function(e,t){var l=e.components,r=e.mdxType,a=e.originalType,p=e.parentName,u=i(e,["components","mdxType","originalType","parentName"]),c=k(l),s=r,m=c["".concat(p,".").concat(s)]||c[s]||d[s]||a;return l?n.createElement(m,o(o({ref:t},u),{},{components:l})):n.createElement(m,o({ref:t},u))}));function m(e,t){var l=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var a=l.length,o=new Array(a);o[0]=s;var i={};for(var p in t)hasOwnProperty.call(t,p)&&(i[p]=t[p]);i.originalType=e,i[c]="string"==typeof e?e:r,o[1]=i;for(var k=2;k<a;k++)o[k]=l[k];return n.createElement.apply(null,o)}return n.createElement.apply(null,l)}s.displayName="MDXCreateElement"},4682:(e,t,l)=>{l.r(t),l.d(t,{assets:()=>p,contentTitle:()=>o,default:()=>d,frontMatter:()=>a,metadata:()=>i,toc:()=>k});var n=l(7462),r=(l(7294),l(3905));const a={sidebar_position:1},o="Workcell CLI",i={unversionedId:"documents/workcell-cli",id:"documents/workcell-cli",title:"Workcell CLI",description:"Usage:",source:"@site/docs/documents/workcell-cli.md",sourceDirName:"documents",slug:"/documents/workcell-cli",permalink:"/workcell/zh-Hans/docs/documents/workcell-cli",draft:!1,editUrl:"https://github.com/weanalyze/workcell/edit/main/docs/documents/workcell-cli.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Documents",permalink:"/workcell/zh-Hans/docs/category/documents"}},p={},k=[{value:"<code>deploy</code>",id:"deploy",level:2},{value:"<code>export</code>",id:"export",level:2},{value:"<code>hello</code>",id:"hello",level:2},{value:"<code>new</code>",id:"new",level:2},{value:"<code>pack</code>",id:"pack",level:2},{value:"<code>serve</code>",id:"serve",level:2},{value:"<code>teardown</code>",id:"teardown",level:2},{value:"<code>up</code>",id:"up",level:2},{value:"<code>version</code>",id:"version",level:2}],u={toc:k},c="wrapper";function d(e){let{components:t,...l}=e;return(0,r.kt)(c,(0,n.Z)({},u,l,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"workcell-cli"},"Workcell CLI"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ [OPTIONS] COMMAND [ARGS]...\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Commands"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"deploy"),": Deploy workcell."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"export"),": Package and export a workcell."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"hello"),": Say hello to workcell."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"new"),": Init a new workcell template."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"pack"),": Prepare deployment image for workcell."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"serve"),": Start a HTTP API server for the workcell."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"teardown"),": Teardown workcell deployment."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"up"),": Build->push->deploy a workcell to weanalyze..."),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"version"),": Return workcell version.")),(0,r.kt)("h2",{id:"deploy"},(0,r.kt)("inlineCode",{parentName:"h2"},"deploy")),(0,r.kt)("p",null,"Deploy workcell.\nThis will deploy workcell by workcell.yaml in buidl_dir. Must be running in project folder or given build_dir.\nArgs: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"provider (str): service provider, e.g. huggingface. \n\nbuild_dir (str): project build directory. \n")),(0,r.kt)("p",null,"Return: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"repo_url (str): huggingface repo url.\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ deploy [OPTIONS]\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-b, --build_dir TEXT"),": ","[default: .workcell]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")),(0,r.kt)("h2",{id:"export"},(0,r.kt)("inlineCode",{parentName:"h2"},"export")),(0,r.kt)("p",null,"Package and export a workcell."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ export [OPTIONS] IMPORT_STRING\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"IMPORT_STRING"),": ","[required]")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--format [docker|we|pex|zip|pyz]"),": ","[default: zip]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")),(0,r.kt)("h2",{id:"hello"},(0,r.kt)("inlineCode",{parentName:"h2"},"hello")),(0,r.kt)("p",null,"Say hello to workcell.\nThis will create a ",(0,r.kt)("inlineCode",{parentName:"p"},"hello_workcell")," project dir and serve it."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ hello [OPTIONS]\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")),(0,r.kt)("h2",{id:"new"},(0,r.kt)("inlineCode",{parentName:"h2"},"new")),(0,r.kt)("p",null,"Init a new workcell template.\nThis will create a template dir for workcell deployment."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ new [OPTIONS] PROJECT_NAME\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"PROJECT_NAME"),": ","[required]")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-p, --provider TEXT"),": ","[default: huggingface]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-r, --runtime TEXT"),": ","[default: python3.8]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")),(0,r.kt)("h2",{id:"pack"},(0,r.kt)("inlineCode",{parentName:"h2"},"pack")),(0,r.kt)("p",null,"Prepare deployment image for workcell.\nThis will create a deployment folder and build docker image. "),(0,r.kt)("p",null,"Args: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'import_string (str): import_string, a.k.a workcell entrypoint. \n\n    e.g. import_string = "app:hello_workcell" \n\nworkcell_provider (str): workcell provider. \n\n    e.g. workcell_provider = "huggingface" \n    \nworkcell_version (str): workcell version. \n\n    e.g. workcell_version = "latest" \n\nworkcell_runtime (str): workcell runtime. \n\n    e.g. workcell_runtime = "python3.8" \n\nworkcell_tags (dict): workcell tags. \n\n    e.g. workcell_tags = \'{"vendor":"aws", "service-type":"http"}\' \n\nworkcell_envs (dict): workcell env. \n\n    e.g. workcell_envs = \'{"STAGE":"latest"}\' \n')),(0,r.kt)("p",null,"Return: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"build_dir (str): project build directory. \n\nworkcell_config (dict): workcell configuration dict. \n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ pack [OPTIONS] IMPORT_STRING\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"IMPORT_STRING"),": ","[required]")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-p, --provider TEXT"),": ","[default: huggingface]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-t, --image TEXT"),": ","[default: ]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-v, --version TEXT"),": ","[default: latest]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-r, --runtime TEXT"),": ","[default: python3.8]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--workcell_tags TEXT"),": ","[default: {}]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--workcell_envs TEXT"),": ","[default: {}]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")),(0,r.kt)("h2",{id:"serve"},(0,r.kt)("inlineCode",{parentName:"h2"},"serve")),(0,r.kt)("p",null,"Start a HTTP API server for the workcell.\nThis will launch a FastAPI server based on the OpenAPI standard and with a automatic interactive documentation."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ serve [OPTIONS] WORKCELL_ENTRYPOINT\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"WORKCELL_ENTRYPOINT"),": ","[required]")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-c, --config PATH")),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-p, --port INTEGER"),": ","[default: 7860]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-h, --host TEXT"),": ","[default: 127.0.0.1]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")),(0,r.kt)("h2",{id:"teardown"},(0,r.kt)("inlineCode",{parentName:"h2"},"teardown")),(0,r.kt)("p",null,"Teardown workcell deployment.\nThis will deploy workcell by workcell.yaml in buidl_dir. Must be running in project folder or given build_dir.\nArgs: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"build_dir (str): project build directory. \n")),(0,r.kt)("p",null,"Return: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"None.\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ teardown [OPTIONS]\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-b, --build_dir TEXT"),": ","[default: .workcell]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")),(0,r.kt)("h2",{id:"up"},(0,r.kt)("inlineCode",{parentName:"h2"},"up")),(0,r.kt)("p",null,"Build->push->deploy a workcell to weanalyze cloud.\nThis will create a deployment folder and build docker image. "),(0,r.kt)("p",null,"Args: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},'import_string (str): import_string, a.k.a workcell fqdn. \n\n    e.g. import_string = "app:hello_workcell" \n\nworkcell_provider (str): workcell provider. \n\n    e.g. workcell_provider = "huggingface" \n    \nworkcell_version (str): workcell version. \n\n    e.g. workcell_version = "latest" \n\nworkcell_runtime (str): workcell runtime. \n\n    e.g. workcell_runtime = "python3.8" \n\nworkcell_tags (dict): workcell tags. \n\n    e.g. workcell_tags = \'{"vendor":"aws", "service-type":"http"}\' \n\nworkcell_envs(dict): workcell env. \n\n    e.g. workcell_envs = \'{"STAGE":"latest"}\' \n')),(0,r.kt)("p",null,"Return: "),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},"build_dir (str): project build directory. \n\nworkcell_config (dict): workcell configuration dict. \n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ up [OPTIONS] IMPORT_STRING\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Arguments"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"IMPORT_STRING"),": ","[required]")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-p, --provider TEXT"),": ","[default: huggingface]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-v, --version TEXT"),": ","[default: latest]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"-r, --runtime TEXT"),": ","[default: python3.8]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--workcell_tags TEXT"),": ","[default: {}]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--workcell_envs TEXT"),": ","[default: {}]"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")),(0,r.kt)("h2",{id:"version"},(0,r.kt)("inlineCode",{parentName:"h2"},"version")),(0,r.kt)("p",null,"Return workcell version.\nThis will return the version of workcell package."),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Usage"),":"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-console"},"$ version [OPTIONS]\n")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Options"),":"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("inlineCode",{parentName:"li"},"--help"),": Show this message and exit.")))}d.isMDXComponent=!0}}]);