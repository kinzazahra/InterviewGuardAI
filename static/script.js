document.addEventListener("visibilitychange", () => {

    if(document.hidden){

        fetch("/tab_switch", {
            method: "POST"
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
        });

    }

});