"use strict";(self.webpackChunkworkcell_doc=self.webpackChunkworkcell_doc||[]).push([[3198],{3905:(e,n,t)=>{t.d(n,{Zo:()=>u,kt:()=>g});var r=t(7294);function o(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function l(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){o(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function i(e,n){if(null==e)return{};var t,r,o=function(e,n){if(null==e)return{};var t,r,o={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(o[t]=e[t]);return o}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(o[t]=e[t])}return o}var c=r.createContext({}),p=function(e){var n=r.useContext(c),t=n;return e&&(t="function"==typeof e?e(n):l(l({},n),e)),t},u=function(e){var n=p(e.components);return r.createElement(c.Provider,{value:n},e.children)},s="mdxType",d={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},m=r.forwardRef((function(e,n){var t=e.components,o=e.mdxType,a=e.originalType,c=e.parentName,u=i(e,["components","mdxType","originalType","parentName"]),s=p(t),m=o,g=s["".concat(c,".").concat(m)]||s[m]||d[m]||a;return t?r.createElement(g,l(l({ref:n},u),{},{components:t})):r.createElement(g,l({ref:n},u))}));function g(e,n){var t=arguments,o=n&&n.mdxType;if("string"==typeof e||o){var a=t.length,l=new Array(a);l[0]=m;var i={};for(var c in n)hasOwnProperty.call(n,c)&&(i[c]=n[c]);i.originalType=e,i[s]="string"==typeof e?e:o,l[1]=i;for(var p=2;p<a;p++)l[p]=t[p];return r.createElement.apply(null,l)}return r.createElement.apply(null,t)}m.displayName="MDXCreateElement"},9328:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>c,contentTitle:()=>l,default:()=>d,frontMatter:()=>a,metadata:()=>i,toc:()=>p});var r=t(7462),o=(t(7294),t(3905));const a={sidebar_position:4},l="Deploy your workcell",i={unversionedId:"guides/deploy-your-workcell",id:"guides/deploy-your-workcell",title:"Deploy your workcell",description:"You can deploy your workcell to Hugging Face Spaces in 1-click! You'll be able to access your workcell from anywhere and share it with your team and collaborators.",source:"@site/docs/guides/deploy-your-workcell.md",sourceDirName:"guides",slug:"/guides/deploy-your-workcell",permalink:"/workcell/zh-Hans/docs/guides/deploy-your-workcell",draft:!1,editUrl:"https://github.com/weanalyze/workcell/edit/main/docs/guides/deploy-your-workcell.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{sidebar_position:4},sidebar:"tutorialSidebar",previous:{title:"Workcell integration",permalink:"/workcell/zh-Hans/docs/guides/workcell-integration"},next:{title:"Congratulations!",permalink:"/workcell/zh-Hans/docs/guides/congratulations"}},c={},p=[{value:"Prepare a Hugging Face account",id:"prepare-a-hugging-face-account",level:2},{value:"Deploy your workcell to Hugging Face",id:"deploy-your-workcell-to-hugging-face",level:2},{value:"Workcell management",id:"workcell-management",level:2},{value:"More details",id:"more-details",level:2}],u={toc:p},s="wrapper";function d(e){let{components:n,...t}=e;return(0,o.kt)(s,(0,r.Z)({},u,t,{components:n,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"deploy-your-workcell"},"Deploy your workcell"),(0,o.kt)("p",null,"You can deploy your workcell to ",(0,o.kt)("a",{parentName:"p",href:"https://huggingface.co/spaces"},"Hugging Face Spaces")," in 1-click! You'll be able to access your workcell from anywhere and share it with your team and collaborators."),(0,o.kt)("h2",{id:"prepare-a-hugging-face-account"},"Prepare a Hugging Face account"),(0,o.kt)("p",null,"First you need a ",(0,o.kt)("a",{parentName:"p",href:"http://huggingface.co/"},"Hugging Face")," account, and prepare your ",(0,o.kt)("inlineCode",{parentName:"p"},"Username")," and ",(0,o.kt)("inlineCode",{parentName:"p"},"User Access Token"),"."),(0,o.kt)("p",null,"Set environment variables like below:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"export HUGGINGFACE_USERNAME={huggingface_username}\nexport HUGGINGFACE_TOKEN={huggingface_token}\n")),(0,o.kt)("p",null,"Replace ",(0,o.kt)("inlineCode",{parentName:"p"},"{huggingface_username}")," with your actual Hugging Face ",(0,o.kt)("inlineCode",{parentName:"p"},"Username"),", and ",(0,o.kt)("inlineCode",{parentName:"p"},"{huggingface_token}")," with your actual ",(0,o.kt)("inlineCode",{parentName:"p"},"User Access Token")," (format like ",(0,o.kt)("inlineCode",{parentName:"p"},"hf_xxx"),"). "),(0,o.kt)("p",null,"You can also store these environment variables in a ",(0,o.kt)("inlineCode",{parentName:"p"},".env")," file in your project folder for convenience."),(0,o.kt)("h2",{id:"deploy-your-workcell-to-hugging-face"},"Deploy your workcell to Hugging Face"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},"Wrap your function with ",(0,o.kt)("inlineCode",{parentName:"p"},"workcell.create_app")," like example above")),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("p",{parentName:"li"},"In your project folder, package your workcell app using the following command:"))),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"workcell pack app:hello_workcell\n")),(0,o.kt)("admonition",{type:"tip"},(0,o.kt)("p",{parentName:"admonition"},(0,o.kt)("inlineCode",{parentName:"p"},"pack")," command will package your function with a ",(0,o.kt)("inlineCode",{parentName:"p"},"Dockerfile")," template into ",(0,o.kt)("inlineCode",{parentName:"p"},".workcell")," folder in your project folder.")),(0,o.kt)("p",null,"Once packaged, deploy your workcell app using the following command:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"workcell deploy\n")),(0,o.kt)("p",null,"\ud83e\udd17 Voila! The deployment process will start, and within a few minutes, your workcell will be available on Hugging Face Spaces, accessible by a unique URL."),(0,o.kt)("h2",{id:"workcell-management"},"Workcell management"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("p",{parentName:"li"},"You can monitor the deployment process and the logs in your terminal, and the deployment status will be shown in your Hugging Face Spaces repo.")),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("p",{parentName:"li"},"You can deploy multiple workcells, and they will be listed in your ",(0,o.kt)("a",{parentName:"p",href:"https://huggingface.co/spaces"},"Hugging Face Spaces")," account, you can manage them from there.")),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("p",{parentName:"li"},"You can also configure various deployment options like environment variables, system requirements, custom domain, etc., by using command line options or a ",(0,o.kt)("inlineCode",{parentName:"p"},"workcell.yaml")," from ",(0,o.kt)("inlineCode",{parentName:"p"},".workcell")," dir in your project folder."))),(0,o.kt)("h2",{id:"more-details"},"More details"),(0,o.kt)("p",null,"You can check ",(0,o.kt)("strong",{parentName:"p"},(0,o.kt)("a",{parentName:"strong",href:"../documents/workcell-cli"},"workcell-cli docs"))," for more details."))}d.isMDXComponent=!0}}]);