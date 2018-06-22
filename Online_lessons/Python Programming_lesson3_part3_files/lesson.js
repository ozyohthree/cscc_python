document.domain = "cscc.edu"
var parentBody = window.parent.document.body;

$(document).ready(function() {
	$.ajaxSetup({
		error: function(xhr, status, error) {
			alert("An AJAX error occured: " + status + "\nError: " + error);
		}
	});
	get_user();
	load_actions();
	
/*	$("div>code").addClass("python").wrap("<pre></pre>");
	$("div>pre code").each(function(i, block) {
		hljs.highlightBlock(block);
	});
*/
	
	var varFrame = get_frame().id;
	$("#"+varFrame, parentBody).height($("#content").height()+100);
});
function load_actions() {
	var varCurrentExercise = "";
	$("a.exercise").click(function(e) {
		e.preventDefault();
		varCurrentExercise = $(this).attr("id");
	});
	$('body').on('DOMNodeRemoved', '.lity', function() {
		check_exercise(varCurrentExercise)
	});
}
function get_user() {
	var varUser = get_querystring("u");
	var varCourse = get_querystring("c");
	var varRole = get_querystring("r");
			
	if(varUser=="") {
		varUser = "guest";
	}
	
	if(varCourse=="") {
		varCourse = "online";
	}
	
	if(varRole=="") {
		varRole = "student";
	}

	if(supports_html5_storage()) {
		localStorage.setItem("itst-2252-name", varUser);
		localStorage.setItem("itst-2252-course", varCourse);
		localStorage.setItem("itst-2252-role", varRole);
	}
	
	Cookies.set('itst-2252-name', varUser);
	Cookies.set('itst-2252-course', varCourse);
	Cookies.set('itst-2252-role', varRole);
	
	save_progress({"lesson":window.location.pathname.match(/.*\/([^/]+)\.([^?]+)/i)[1].replace(".htm","")});
	apply_id();
}
function save_progress(args) {
	//{type:lesson|topic|section, lesson:varLesson, topic:varTopic, section:varSection}
//	var varUsername = localStorage.getItem("itst-2252-name");
//	var varCourse = localStorage.getItem("itst-2252-course");
	var varUsername = Cookies.get('itst-2252-name');
	var varCourse = Cookies.get('itst-2252-course');
	if(typeof args.section === "undefined") {
		args.section = "";
	}
	if(typeof args.topic === "undefined") {
		args.topic = "";
	}
	if(typeof args.lesson === "undefined") {
		args.lesson = "";
	}
	var varSuccess = "failure";
	$.ajax({
		type: "POST",
		url : "https://online.cscc.edu/apps/python/book/_scripts/lesson.php",
		data: {
			"U" : varUsername,
			"C" : varCourse,
			"L" : args.lesson,
			"T" : args.topic,
			"S" : args.section
		},
		success : function (data) {
			varSuccess = "success";
		},
		error: function (xhr, ajaxOptions, thrownError) {
			//alert(xhr.status+" - "+thrownError);
		}
	});
	return varSuccess;
}
function apply_id() {
	var varUser = Cookies.get('itst-2252-name');
	var varCourse = Cookies.set('itst-2252-course');
	var varRole = Cookies.set('itst-2252-role');
	
	var varQueryString = "u="+varUser+"&c="+varCourse+"&r="+varRole;
	
	$("a.exercise").each(function() {
		var varURL = $(this).attr("href");
		if(varURL.indexOf("?") == -1) {
			$(this).attr("href",varURL+"?"+ varQueryString);
		} else {
			$(this).attr("href",varURL+"&"+ varQueryString);
			var varExercise = $(this).attr("id");
			check_exercise(varExercise);
		}
	});
}
function check_exercise(varExercise) {
	
	var varUser = Cookies.get('itst-2252-name');
	var varCourse = Cookies.set('itst-2252-course');
	
	var varStatus = "";
	
	$.get("https://online.cscc.edu/apps/python/book/_scripts/exercise.php", {user: varUser, course: varCourse, exercise: varExercise})
		.done(function(data) {
			if(data != "") {
				$("#"+varExercise).parent().find(".confirmation").remove();
				var varClass = "good";
				if(data.indexOf("not yet")>0) {
					varClass = "bad";
				}
				$("#"+varExercise).parent().append("<div class='confirmation "+varClass+"'>"+data+"</div>");
			}
		});
}
function get_querystring(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]"+name+"=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}
function get_frame() {
    var iframes = parent.document.getElementsByTagName('iframe');
    for (var i = iframes.length; i-->0;) {
        var iframe= iframes[i];
        try {
            var idoc= 'contentDocument' in iframe? iframe.contentDocument : iframe.contentWindow.document;
        } catch (e) {
            continue;
        }
        if (idoc===document)
            return iframe;
    }
    return false;
}
function supports_html5_storage(){
    try {
        return 'localStorage' in window && window['localStorage'] !== null;
    } catch(e) {
        return false;
    }
}