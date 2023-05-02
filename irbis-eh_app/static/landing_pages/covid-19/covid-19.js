const partsOfWorld = [
    "north_america",
    "south_america",
    "eurasia",
    "africa",
    "australia",
]

window.addEventListener('load', function() {

    const mapElements = {}

    for (let name of partsOfWorld) {

        let svg_obj = document.querySelector(`#${name + "_obj"}`).contentDocument;
        let block_id = document.querySelector(`#${name + "_card"}`);
        let svg_paths = svg_obj.querySelectorAll("path");


        mapElements[name] = {svg_paths: svg_paths, block_id: block_id}
    }

    Object.keys(mapElements).forEach((key) => {
        mapElements[key].block_id.style.transition = "background-color 0.4s ease-in-out";
        for(let item of mapElements[key].svg_paths) {
            item.addEventListener("mouseover", function() {
                for(let i of mapElements[key].svg_paths) {
                    i.style.fill = "#167C51";
                }
                let h2_els = mapElements[key].block_id.getElementsByTagName("h2");
                for (let elem of h2_els) {
                    console.log(elem);
                    elem.style.color = "#167C51";
                }
            })
            item.addEventListener("mouseout", function() {
                for(let i of mapElements[key].svg_paths) {
                    i.style.fill = "#FB4C47";
                }
                // mapElements[key].block_id.style.backgroundColor = "";
                let h2_els = mapElements[key].block_id.getElementsByTagName("h2");
                for (let elem of h2_els) {
                    console.log(elem);
                    elem.style.color = "#FB4C47";
                }
            })
        }
        mapElements[key].block_id.addEventListener("mouseover", function() {
            let h2_els = mapElements[key].block_id.getElementsByTagName("h2");
            for (let elem of h2_els) {
                elem.style.color = "#167C51";
            }
            for(let item of mapElements[key].svg_paths) {
                item.style.fill = "#167C51";
            }
        })
        mapElements[key].block_id.addEventListener("mouseout", function() {
            let h2_els = mapElements[key].block_id.getElementsByTagName("h2");
            for (let elem of h2_els) {
                console.log(elem);
                elem.style.color = "#FB4C47";
            }
            for(let item of mapElements[key].svg_paths) {
                item.style.fill = "#FB4C47";
            }
        })
    })

    document.querySelector('form').addEventListener('submit', submitForm);

    document.getElementById("close_popup").addEventListener("click", function() {
        var popupMessage = document.getElementById("myPopup");
        closePopup(popupMessage);
    });

    function submitForm(event) {
        event.preventDefault();

        var form = document.getElementById("input_email");
        var email = document.getElementById("email");
        var emailValidationMessage = document.getElementById("emailValidationMessage");
        var popupMessage = document.getElementById("myPopup");

        if (form.checkValidity() === false) {
            emailValidationMessage.style.display = "inline-block";
        } else {
            emailValidationMessage.style.display = "none";
            openPopup(popupMessage);
        }
    }

    function openPopup(Obj) {
        Obj.style.display = "block";
    }

    function closePopup(Obj) {
        Obj.style.display = "none";
    }

    const virusImg1 = document.querySelector('.overlay_virus_img_1');
    const virusImg2 = document.querySelector('.overlay_virus_img_2');

    window.addEventListener('scroll', () => {
        virusImg1.style.transform = `translate(${Math.random()*4-2}px, ${Math.random()*4-2}px)`;
        virusImg2.style.transform = `translate(${Math.random()*4-2}px, ${Math.random()*4-2}px)`;
    });

});



