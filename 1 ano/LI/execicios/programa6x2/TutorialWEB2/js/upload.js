// Image UpLoad Javascript
var file;

function updatePhoto(event) {
	var reader = new FileReader();
	reader.onload = function(event) {
		//Create an imagem
		var img = new Image();
		img.onload = function() {
			//Put imagen on screen
			const canvas = $("#photo")[0];
			const ctx = canvas.getContext("2d");
			ctx.drawImage(img,0,0,img.width,img.height,0,0,550, 450);
		}
		img.src = event.target.result;
	}

	file = event.target.files[0];
	//Obtain the file
	reader.readAsDataURL(file);
}

function uploadImage() {
    if(file != null) {
        sendFile(file); //<----problem here 25 -> 32
        //Release the resources alocated to the selected image 
        window.URL.revokeObjectURL(picURL);    
    }
    else alert("Missing image!");
}

function sendFile(file) {
	var data = new FormData();
	data.append("myFile", file); //here is image????????????

	////////////////////////////////
	//var name =$("#nameImg").val();
	//data.append("nameImg,name");

	//var author =$("#authorImg").val();
	//data.append("authorImg,name");


	//var name = file.name;
	//var author = file.author;
	//sumthing got in the var????????????????
	
	////////////////////////////////
	//Obtain nameImg and authorImg and fill the form
	var name =$("#nameImg").val();
	data.append("nameImg",name);

	var author =$("#authorImg").val();
	data.append("authorImg",author);				
	
	//sumthing got in the var????????????????
	if (name == "" || author == "") alert("Missing name and/or author!"); //<- stuck here 32 ->42
	else {
		var xhr = new XMLHttpRequest();
		xhr.open("POST", "/upload"); //open python upload
		xhr.upload.addEventListener("progress", updateProgress(this), false); //create the sending data
		xhr.send(data); //where is sending?????? at app.py
	}
}

function updateProgress(evt){
	if(evt.loaded == evt.total) alert("Okay");
}
