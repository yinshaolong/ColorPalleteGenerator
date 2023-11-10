const form = document.querySelector("#form");
form.addEventListener("submit", (event) => {
    // stops the form from submitting/referesing the page
    event.preventDefault();
    getColors();
});

function getColors(){
        // form.elements gets all of the references to the form (i.e. query)
        const queryForm = form.elements.query.value;
        //send request
        fetch("/palette", {
            method: "POST",
            headers: {
                // tells the server what type of data we are sending
                "Content-Type": "application/x-www-form-urlencoded"
            },
            // URLSearchParams is a built in class that allows us to create a query string
            body: new URLSearchParams({
                query: queryForm
            })
        }).then((response) => {
            return response.json();
        }).then((data) => {
            console.log(data.colors);
            const colors = data.colors;
            const container = document.querySelector(".container");
            createColorBlocks(colors, container);
        })
}

function createColorBlocks(colors, container){
    container.innerHTML = "";
    colors.forEach((color) => {
        const div = document.createElement("div");
        //gives div the class of color
        div.classList.add("color")
        div.style.backgroundColor = color;
        //makes clicking on div copy to clipboard
        div.addEventListener("click", ()=>{
            navigator.clipboard.writeText(color);
        })

        //use side ticks instead of single quotes
        div.style.width = `calc(100%/ ${colors.length})`;
        //adds text (the color) to the div
        const span = document.createElement("span");
        span.innerText = color;
        div.appendChild(span);
        container.appendChild(div);
    })
    
}