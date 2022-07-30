(function () {

	if (!window.$) {
		console.warn('qcmain::loader:\n\tjquery don\'t be loaded first!');
		return;
	}

	var COMPLETED = 1;
	var step = 0;

	function loadScript (src, callback) {
		var script = document.createElement('script');
		script.onerror = function (error) { callback(error, null); };
		script.onload = function () { callback(null, null); };
		script.src = src;
		document.head.appendChild(script);
	}

	function loadScriptCallback (error) {
		step++;
		if (error) {
			return;
		}
		if (step === COMPLETED && window.QCComponent) {
			window.QCComponent.init();
		}
	}

	var logicalScript = "//imgcache.qq.com/qcloud/main/scripts/release/qccomponent/index.e8bc071c94dec0d494f6.js?max_age=31536000";
	loadScript(logicalScript, loadScriptCallback);
})();
