!function(t){function e(o){if(n[o])return n[o].exports;var r=n[o]={exports:{},id:o,loaded:!1};return t[o].call(r.exports,r,r.exports,e),r.loaded=!0,r.exports}var n={};return e.m=t,e.c=n,e.p="//<%=CSS_DOMAIN%>/qcloud/main/scripts/",e(0)}({0:function(t,e,n){"use strict";n("K+qK"),n("tAlG"),n("XAob"),n("X7kb")},"K+qK":function(t,e,n){"use strict";var o=n("3but"),r=n("xuqg").sessionStorage,c=o.getCookieDomain(),i="https://"+o.getRealHostname(),a=(encodeURIComponent(location.href),n("3but").getCDNDomain());!function(){var t=document.createElement("script");t.src=location.protocol+"//"+a+"/qcloud/platreport/dest/index.js";var e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(t,e)}(),function(t){t({},{},{})}(function(t,e,n){function o(t,e){var n=(65535&t)+(65535&e),o=(t>>16)+(e>>16)+(n>>16);return o<<16|65535&n}function u(t,e){return t<<e|t>>>32-e}function l(t,e,n,r,c,i){return o(u(o(o(e,t),o(r,i)),c),n)}function s(t,e,n,o,r,c,i){return l(e&n|~e&o,t,e,r,c,i)}function d(t,e,n,o,r,c,i){return l(e&o|n&~o,t,e,r,c,i)}function m(t,e,n,o,r,c,i){return l(e^n^o,t,e,r,c,i)}function f(t,e,n,o,r,c,i){return l(n^(e|~o),t,e,r,c,i)}function p(t,e){t[e>>5]|=128<<e%32,t[(e+64>>>9<<4)+14]=e;var n,r,c,i,a,u=1732584193,l=-271733879,p=-1732584194,g=271733878;for(n=0;n<t.length;n+=16)r=u,c=l,i=p,a=g,u=s(u,l,p,g,t[n],7,-680876936),g=s(g,u,l,p,t[n+1],12,-389564586),p=s(p,g,u,l,t[n+2],17,606105819),l=s(l,p,g,u,t[n+3],22,-1044525330),u=s(u,l,p,g,t[n+4],7,-176418897),g=s(g,u,l,p,t[n+5],12,1200080426),p=s(p,g,u,l,t[n+6],17,-1473231341),l=s(l,p,g,u,t[n+7],22,-45705983),u=s(u,l,p,g,t[n+8],7,1770035416),g=s(g,u,l,p,t[n+9],12,-1958414417),p=s(p,g,u,l,t[n+10],17,-42063),l=s(l,p,g,u,t[n+11],22,-1990404162),u=s(u,l,p,g,t[n+12],7,1804603682),g=s(g,u,l,p,t[n+13],12,-40341101),p=s(p,g,u,l,t[n+14],17,-1502002290),l=s(l,p,g,u,t[n+15],22,1236535329),u=d(u,l,p,g,t[n+1],5,-165796510),g=d(g,u,l,p,t[n+6],9,-1069501632),p=d(p,g,u,l,t[n+11],14,643717713),l=d(l,p,g,u,t[n],20,-373897302),u=d(u,l,p,g,t[n+5],5,-701558691),g=d(g,u,l,p,t[n+10],9,38016083),p=d(p,g,u,l,t[n+15],14,-660478335),l=d(l,p,g,u,t[n+4],20,-405537848),u=d(u,l,p,g,t[n+9],5,568446438),g=d(g,u,l,p,t[n+14],9,-1019803690),p=d(p,g,u,l,t[n+3],14,-187363961),l=d(l,p,g,u,t[n+8],20,1163531501),u=d(u,l,p,g,t[n+13],5,-1444681467),g=d(g,u,l,p,t[n+2],9,-51403784),p=d(p,g,u,l,t[n+7],14,1735328473),l=d(l,p,g,u,t[n+12],20,-1926607734),u=m(u,l,p,g,t[n+5],4,-378558),g=m(g,u,l,p,t[n+8],11,-2022574463),p=m(p,g,u,l,t[n+11],16,1839030562),l=m(l,p,g,u,t[n+14],23,-35309556),u=m(u,l,p,g,t[n+1],4,-1530992060),g=m(g,u,l,p,t[n+4],11,1272893353),p=m(p,g,u,l,t[n+7],16,-155497632),l=m(l,p,g,u,t[n+10],23,-1094730640),u=m(u,l,p,g,t[n+13],4,681279174),g=m(g,u,l,p,t[n],11,-358537222),p=m(p,g,u,l,t[n+3],16,-722521979),l=m(l,p,g,u,t[n+6],23,76029189),u=m(u,l,p,g,t[n+9],4,-640364487),g=m(g,u,l,p,t[n+12],11,-421815835),p=m(p,g,u,l,t[n+15],16,530742520),l=m(l,p,g,u,t[n+2],23,-995338651),u=f(u,l,p,g,t[n],6,-198630844),g=f(g,u,l,p,t[n+7],10,1126891415),p=f(p,g,u,l,t[n+14],15,-1416354905),l=f(l,p,g,u,t[n+5],21,-57434055),u=f(u,l,p,g,t[n+12],6,1700485571),g=f(g,u,l,p,t[n+3],10,-1894986606),p=f(p,g,u,l,t[n+10],15,-1051523),l=f(l,p,g,u,t[n+1],21,-2054922799),u=f(u,l,p,g,t[n+8],6,1873313359),g=f(g,u,l,p,t[n+15],10,-30611744),p=f(p,g,u,l,t[n+6],15,-1560198380),l=f(l,p,g,u,t[n+13],21,1309151649),u=f(u,l,p,g,t[n+4],6,-145523070),g=f(g,u,l,p,t[n+11],10,-1120210379),p=f(p,g,u,l,t[n+2],15,718787259),l=f(l,p,g,u,t[n+9],21,-343485551),u=o(u,r),l=o(l,c),p=o(p,i),g=o(g,a);return[u,l,p,g]}function g(t){var e,n="";for(e=0;e<32*t.length;e+=8)n+=String.fromCharCode(t[e>>5]>>>e%32&255);return n}function w(t){var e,n=[];for(n[(t.length>>2)-1]=void 0,e=0;e<n.length;e+=1)n[e]=0;for(e=0;e<8*t.length;e+=8)n[e>>5]|=(255&t.charCodeAt(e/8))<<e%32;return n}function v(t){return g(p(w(t),8*t.length))}function h(t,e){var n,o,r=w(t),c=[],i=[];for(c[15]=i[15]=void 0,r.length>16&&(r=p(r,8*t.length)),n=0;n<16;n+=1)c[n]=909522486^r[n],i[n]=1549556828^r[n];return o=p(c.concat(w(e)),512+8*e.length),g(p(i.concat(o),640))}function y(t){var e,n,o="0123456789abcdef",r="";for(n=0;n<t.length;n+=1)e=t.charCodeAt(n),r+=o.charAt(e>>>4&15)+o.charAt(15&e);return r}function b(t){return unescape(encodeURIComponent(t))}function S(t){return v(b(t))}function q(t){return y(S(t))}function x(t,e){return h(b(t),b(e))}function E(t,e){return y(x(t,e))}function T(t,e,n){return e?n?x(e,t):E(e,t):n?S(t):q(t)}function _(t){var e=new RegExp("(^| )"+decodeURIComponent(t)+"(?:=([^;]*))?(;|$)"),n=document.cookie.match(e);return n?n[2]?decodeURIComponent(n[2]):"":null}function N(t,e,n,o,r,c){var i=new Date,n=arguments[2]||null,o=arguments[3]||"/",r=arguments[4]||null,c=arguments[5]||!1;n?i.setMinutes(i.getMinutes()+parseInt(n)):"",document.cookie=encodeURIComponent(t)+"="+encodeURIComponent(e)+(n?";expires="+i.toGMTString():"")+(o?";path="+o:"")+(r?";domain="+r:"")+(c?";secure":"")}function A(){var t=_("uin");return t&&(t=t.replace(/^o(0)*/gi,"")),t}function C(t,e){var n=arguments[1]||window.location.search,o=new RegExp("(^|&)"+t+"=([^&]*)(&|$)"),r=n.substr(n.indexOf("?")+1).match(o);return null!=r?r[2]:""}function O(t,e,n){function o(t,e){return function(){return t.apply(e,arguments)}}if(t&&e&&n)if(t instanceof Array)for(var r=0,c=t.length;r<c;r++)O(t[r],e,n);else if(e instanceof Array)for(var r=0,c=e.length;r<c;r++)O(t,e[r],n);else if(window.addEventListener){var i=o(n,t);t.addEventListener(e,i,!1)}else if(window.attachEvent){var i=o(n,t);t.attachEvent("on"+e,i)}else t["on"+e]=n}function D(t,e,n){var t=window.event||t,o=t.srcElement||t.target;return o}function I(t,e){var n={};for(var o in t)t.hasOwnProperty(o)&&(n[o]=t[o]);for(var r in e)e.hasOwnProperty(r)&&(n[r]=e[r]);return n}function k(){var t=T(Math.random()+"_"+Y+"_"+J+"_"+nt+"_"+tt+"_"+navigator.appName+"_"+navigator.userAgent+"_"+(new Date).getTime());return N("qcloud_visitId",t,"","/",c),t}function L(){if(r.isSupport()){var t=r.get("landingpage");return t?t:(r.set("landingpage",location.href),location.href)}if(_("landingpage"))return _("landingpage");var e=location.href.substr(0,200);return N("landingpage",e,"","/",c),e}function R(t,e){if("string"==typeof t)var t=t;else if(e=t,location.hostname.indexOf("qcloud.com")!=-1)var t="https://ping.qcloud.com/trafficCollect.php";else var t="https://ping.cloud.tencent.com/trafficCollect.php";"hotrep"!=e.expKey||window.TCISD||R({expKey:"tcssHotrep",expValue:e.expValue}),"tcssHotrep"==e.expKey?(e=I(e,{dm:"www.qcloud.com.hot",url:location.pathname,tt:"-",hottag:e.expValue,hotx:9999,hoty:9999}),delete e.expKey,delete e.expValue,t="https://pingfore.qq.com/pingd"):e=I(e,lt),e.t=(new Date).getTime();var n=document.createElement("img"),o=[];for(var r in e)o.push(r+"="+encodeURIComponent(e[r]));n.onload=n.onerror=function(){n=n.onload=n.onerror=null},n.src=t+(t.indexOf("?")<0?"?":"&")+o.join("&")}function j(){return document.referrer||""}function U(t){var e={sogou:[/^http(s)?:\/\/(www|m)\.sogou.com\/bill_cpc/],baidu:[/^http(s)?:\/\/bzclk\.baidu\.com\/adrc\.php/,/http(s)?:\/\/cpro\.baidu\.com/,/http(s)?:\/\/www\.baidu\.com\/baidu\.php/],google:[/^http(s)?:\/\/www\.googleadservices\.com\/pagead\/aclk/]},n={baidu:[/^http(s)?:\/\/www\.baidu\.com/,/^http(s)?:\/\/m\.baidu\.com/],google:[/^http(s)?:\/\/[^\.]+\.google\./],sogou:[/^http(s)?:\/\/(www|m)\.sogou\.com/],bing:[/^http(s)?:\/\/[^\.]+\.bing\.com/],sm:[/^http(s)?:\/\/(.+)\.sm\.cn/],360:[/^http(s)?:\/\/[^\.]+\.so\.com/]},o=j(),r="sem"==t?e:n,c=null;for(var i in r)for(var a=0;a<r[i].length;a++)if(r[i][a].test(o)){c=i;break}return c?["qcloud",c,t].join("."):""}function B(){var t=_("qcloud_from")||"";return t.indexOf("-")!==-1&&(t=t.split("-")[0]),t}function M(){var t=/^https:\/\/www.qcloud.com\/login(\/)?(\?.*)?$/,e=/^https:\/\/(intl.)?cloud.tencent.com\/login(\/)?(\?.*)?$/,n=location.href;if(t.test(n)||e.test(n)){var o=decodeURIComponent(C("s_url"));if(o&&C("fromSource",o)&&/^\w+\.\d+\.\d+\.\d+$/.test(C("fromSource",o)))return C("fromSource",o)}return""}function K(){var t=location.href,e=/^https:\/\/(www.qcloud.com|cloud.tencent.com)\/community/;return!!e.test(t)}function P(t){return t=t||j(),!/^http(s)?:\/\/(.)+(\.qcloud\.com|\.tencent\.com|\.qq\.com|\.dnspod\.cn)/.test(t)}function F(t){return t=t||j(),/^http(s)?:\/\/afpeng\.alimama\.com\/ex/.test(t)}function H(){var t="qcloud.directEnter.",e=location.hostname;try{if("cloud.tencent.com"==e||"www.qcloud.com"==e||"intl.cloud.tencent.com"==e){var n=location.pathname.split("/");n=n&&n.length>=2&&n[1]?n[1]:"home",t+=n}else t+=e;return t}catch(t){return"qcloud.directEnter"}}function V(){var t=C("fromSource"),e=B(),n=j(),o=H(),r="qcloud.outsideSite",c="gwzcw.59957.59957.59957",i="gwzcw.711973.711973.711973";if(t?/^\w+\.\d+\.\d+\.\d+$/.test(t)||(t=""):t=M(),t)return Q(t)&&e?Q(e)&&e!=r?t:e:t;if(n){var a=U("sem")||U("seo");return F(n)?e?e:i:P(n)&&K()?e?e:c:a?a:P(n)&&(Q(e)||!e)?r:e}return e?e:K()?c:o}function $(){var t=C("from")||"",e=_("from")||"";return t&&t.length<=50&&N("from",t,2880,"/",c),t||e}function G(t){t+="-"+(new Date).getTime(),N("qcloud_from",t,43200,"/",c);var e=new Image,n={".cloud.tencent.com":"www.qcloud.com",".qcloud.com":"cloud.tencent.com"},o="/services/sync/cookie";e.onload=e.onerror=function(){e=e.onload=e.onerror=null};var r=n[c];r&&(r="https://"+r+o+"?qcloud_from="+t,e.src=r)}function Q(t){return t&&/^qcloud\./.test(t)}function z(t){var e=100;return t!=B()&&t.length&&t.length<=e}function X(t){var e=i+"/services/ajax/report_channel",n={type:"browse",uin:Y,channelId:t,referer:J,t:(new Date).getTime()},o=document.createElement("img"),r=[];for(var c in n)r.push(c+"="+encodeURIComponent(n[c]));o.onload=o.onerror=function(){o=o.onload=o.onerror=null},o.src=e+"?"+r.join("&")}function Z(t){return dt&&!mt.test(t)?"m."+t:dt?t:t.replace(mt,"")}function W(){gt&&new Date-ft<50||pt||(pt=!0,R({expKey:"stayTime",expValue:(new Date).getTime()-et}))}var Y=A()||"",J=j(),tt=location.href,et=(new Date).getTime(),nt=V()||H(),ot=$()||"",rt=_("qcloud_visitId")||k(),ct=_("language")||"",it=_("lastLoginType")||"",at=_("_ga")||"",ut=document.title||"";z(nt)&&(G(nt),X(nt));var lt={uin:Y,ul:tt,referer:J,fromSource:nt,visitId:rt,landingpage:L(),language:ct,lastLoginType:it,_ga:at,pageTitle:ut,from:ot,type:"OfficialNetworkTraffic"};window.ignoreReportQcloudStat||R({expKey:"browse",expValue:location.href});var st=navigator.userAgent,dt=(/AppleWebKit.*Mobile/i.test(st)||/MIDP|SymbianOS|NOKIA|SAMSUNG|LG|NEC|TCL|Alcatel|BIRD|DBTEL|Dopod|PHILIPS|HAIER|LENOVO|MOT-|Nokia|SonyEricsson|SIE-|Amoi|ZTE/.test(st))&&!/iPad/i.test(st),mt=/^m\./;O(document.body,"mousedown",function(t){if(0==t.button||1==t.button)for(var e=D(t),n="";e&&"BODY"!=e.tagName&&"HTML"!=e.tagName;){if("TBODY"!=e.tagName&&"THEAD"!=e.tagName&&e.getAttribute&&(!n&&(n=e.getAttribute("hotrep")||e.hotrep||""),!n&&(n=e.getAttribute("data-hotrep")||"")),n){n=Z(n),R({expKey:"hotrep",expValue:n});break}e=e.parentNode}});var ft,pt,gt=window.attachEvent&&!window.opera;gt&&O(document.body,"mouseup",function(t){var e=D(t);1===e.nodeType&&/^ajavascript:/i.test(e.tagName+e.href)&&(ft=new Date)}),O(window,"beforeunload",W),O(window,"unload",W),window.QcloudStat=n.exports={reportAction:R},function(){var t=location.hostname;if(!("www.qcloud.com"!=t&&"cloud.tencent.com"!=t&&"intl.cloud.tencent.com"!=t||K()||window._mtac)){window._mtac={performanceMonitor:1};var e=document.createElement("script");e.src="//pingjs.qq.com/h5/stats.js?v2.0.4",e.setAttribute("name","MTAH5"),e.setAttribute("sid","500505369"),e.setAttribute("cid","500505370");var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(e,n)}}(),function(){var t=document.createElement("script");t.src=location.protocol+"//tajs.qq.com/stats?sId=62716249";var e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(t,e)}(),function(){var t=C("qz_gdt")||C("gdt_vid"),e=i+"/services/ajax/reportGDT",n="";if(t?(N("gdt_click_id",t,"","/",c),n="VIEW_CONTENT"):_("gdt_click_id")&&(t=_("gdt_click_id"),n="CONSULT"),n){var o={action_type:n,url:location.href,user_action_set_id:1106426173,click_id:t};R(e,{data:JSON.stringify(o)})}}(),function(){if(!window.QC_SENSORS){var t=document.createElement("script");t.src=location.protocol+"//"+a+"/qcloud/act/scripts/release/common/addon/sensors.js?max_age=3600";var e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(t,e)}}(),function(){try{var t=_("subAccountLoginPage");t&&t.indexOf("?")!=-1&&(t=t.split("?")[0],N("subAccountLoginPage",t,43200,"/",c))}catch(t){}}()})},"3but":function(t,e){"use strict";var n={getRealHostname:function(){var t=location.hostname;return t.indexOf("qcloud.com")!=-1?"www.qcloud.com":t.indexOf("cloud.tencent.com")!=-1?"cloud.tencent.com":"www.qcloud.com"},getCookieDomain:function(){var t=location.hostname;return t.indexOf("qcloud.com")!=-1?".qcloud.com":t.indexOf("cloud.tencent.com")!=-1?".cloud.tencent.com":".qcloud.com"},getQcmainHostname:function(){var t=location.hostname;return t.indexOf("qcloud.com")!=-1?"www.qcloud.com":t.indexOf("intl.cloud.tencent.com")!=-1?"intl.cloud.tencent.com":t.indexOf("cloud.tencent.com")!=-1?"cloud.tencent.com":"www.qcloud.com"},getCDNDomain:function(){return window.__CDN_DOMAIN||window.QCCDN_HOST||"imgcache.qq.com"}};t.exports=n},xuqg:function(t,e){"use strict";var n={set:function(t,e){if(window.sessionStorage&&"string"==typeof t)try{window.sessionStorage[t]=e}catch(t){}},get:function(t){return window.sessionStorage&&"string"==typeof t?window.sessionStorage[t]:null},isSupport:function(){try{return!!window.sessionStorage&&(window.sessionStorage.isPrivate=!1,!0)}catch(t){return!1}}},o={set:function(t,e){if(window.localStorage&&"string"==typeof t)try{window.localStorage[t]=e}catch(t){}},get:function(t){return window.localStorage&&"string"==typeof t?window.localStorage[t]:null},isSupport:function(){if(!window.localStorage)return!1;try{return window.localStorage.isPrivate=!1,!0}catch(t){return!1}}};t.exports={sessionStorage:n,localStorage:o}},tAlG:function(t,e){"use strict";function n(){!function(t,e,n,o,r){t[o]=t[o]||[],t[o].push({"gtm.start":(new Date).getTime(),event:"gtm.js"});var c=e.getElementsByTagName(n)[0],i=e.createElement(n),a="dataLayer"!=o?"&l="+o:"";i.async=!0,i.src="https://www.googletagmanager.com/gtm.js?id="+r+a,c.parentNode.insertBefore(i,c)}(window,document,"script","dataLayer","GTM-KV8Z8NK")}var o=navigator.userAgent||"",r=/miniprogram/i.test(o);r||(window.$?$(window).on("load",function(){n()}):n())},XAob:function(t,e,n){"use strict";var o=n("3but").getCDNDomain();!function(t,e,n,o,r,c,i){t.GoogleAnalyticsObject=r,t[r]=t[r]||function(){(t[r].q=t[r].q||[]).push(arguments)},t[r].l=1*new Date,c=e.createElement(n),i=e.getElementsByTagName(n)[0],c.async=1,c.src=o,i.parentNode.insertBefore(c,i)}(window,document,"script","//"+o+"/open/qcloud/common/analytics.js?max_age=31536000","ga");var r=navigator.userAgent||"",c=/miniprogram/i.test(r);c||navigator.userAgent.toLowerCase().indexOf("micromessenger")===-1&&("intl.cloud.tencent.com"==location.hostname?(ga("create","UA-104377279-1","auto"),ga("send","pageview")):(ga("create","UA-67744695-1","auto",{allowLinker:!0}),ga("require","linker"),location.hostname.indexOf("qcloud.com")!=-1?ga("linker:autoLink",["cloud.tencent.com"]):ga("linker:autoLink",["qcloud.com"]),ga("send","pageview")))},X7kb:function(t,e,n){"use strict";function o(t){var e={},n=window.performance.timing.navigationStart;for(var o in c.eventFlag)window.performance.timing[o]&&(e[c.eventFlag[o]]=window.performance.timing[o]-n);var r=i.getPageType(location.pathname);return e.flag1=t.domainFlag[0],e.flag2=t.domainFlag[1],e.flag3=t.pageFlag[r],e}function r(){if(window.performance&&window.performance.timing){var t=c.domainConfig[location.host];if(t){var e={appid:c.appid,platform:i.getPlatform(),speedparams:o(t)},n=i.appendEncodedData(location.protocol+"//report.huatuo.qq.com/report.cgi",e);i.insertOneTimeImg(n)}}}var c=n("QTeM"),i=n("ZyNu");"complete"===document.readyState?r():window.addEventListener("load",r)},QTeM:function(t,e){"use strict";e.appid=20373,e.eventFlag={fetchStart:5,domainLookupStart:6,domainLookupEnd:7,connectStart:8,connectEnd:9,requestStart:10,responseStart:11,responseEnd:12},e.domainConfig={"cloud.tencent.com":{domainFlag:[21970,1],pageFlag:{product:2,home:3,solution:4,document:5,customer:6,login:7,others:8}},"intl.cloud.tencent.com":{domainFlag:[21971,1],pageFlag:{product:2,home:3,solution:4,document:5,others:6,login:7}}}},ZyNu:function(t,e){"use strict";var n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t};e.getPlatform=function(){var t=(navigator.userAgent||"").toLowerCase();if(!t)return"";var e=/android|webos|ip(hone|ad|od)|opera (mini|mobi|tablet)|iemobile|windows.+(phone|touch)|mobile|fennec|kindle (Fire)|Silk|maemo|blackberry|playbook|bb10\; (touch|kbd)|Symbian(OS)|Ubuntu Touch/i,n=/ip(hone|ad|od)/i;return e.test(t)?t.indexOf("android")>-1?"android":n.test(t)?"ios":"":"pc"},e.appendEncodedData=function(t,e){var o=[];for(var r in e)if("object"!==n(e[r]))o.push(r+"="+encodeURIComponent(e[r]));else{var c=[];for(var i in e[r])c.push(i+"="+encodeURIComponent(e[r][i]));o.push(r+"="+encodeURIComponent(c.join("&")))}return t+"?"+o.join("&")},e.getPageType=function(t){var e={product:/^\/product\/*/,solution:/^\/solution\/*/,document:/^\/document\/*/,customer:/^\/customer\/*/,login:/^\/login\/*/,home:/^\/(home)?$/};for(var n in e)if(e[n].test(t))return n;return"others"},e.insertOneTimeImg=function(t){var e=document.createElement("img");e.onload=e.onerror=function(){e=e.onload=e.onerror=null},e.src=t}}});