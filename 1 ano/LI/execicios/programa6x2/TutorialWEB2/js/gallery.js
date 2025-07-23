$(document).ready(
	function(){
		imageslist("all");
    });

function imageslist(id) {
	var author;
	if (id == "all") author = "all";
	else {
			author = $("#authorImg").val();
			if (author == "") author = "all";
	}
	$.get("/list",
		{ id : author },
		function(response){
			showimages(response);
		});
}

function showimages(response) {//<-------here
	// response.images is the list of dictionaries with the images information
	$("#showimages").html("");
	for (let i = 0; i < response.images.length; i++) {
		// html code for print the image information
		// html code for showing the image and allow to click on it and invoke function showimagecomments
		///
		let imgData = response.images[i]; // Assuming each entry contains image info
        let imgElement = `
            <div class="image-container">
                <img src="${imgData.path}" alt="${imgData.nameImg}" width="200">
                <p>${imgData.nameImg} by ${imgData.authorImg}</p>
                <button onclick="showimagecomments('${imgData.id}')">Comments</button>
            </div>
        `;
        $("#showimages").append(imgElement);
		///
	}
}

function showimagecomments(id) {
	window.open("../html/image.html?id=" + id, '_blank');
}
