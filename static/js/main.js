function find_camp() {
    let camp = document.querySelector(".home__form--input").value;
    if (!camp) {
        showError();
        return;
    }

    let boot_name = "";
    let boot_img = "";
    let boot_id = "";
    for (let i = 0; i < campList.length; i++) {
        if (campList[i]["name"] === camp) {
            boot_name = campList[i]["name"];
            boot_img = campList[i]["boot_img"];
            boot_id = campList[i]["id"];
            break;
        } else {
            boot_id = false;
        }
    }

    if (boot_id) {
        let targetList = document.querySelectorAll(".card");
        targetList.forEach((target) => {
            let target_id = target.attributes[2].nodeValue;
            if (target_id === boot_id) {
                target.classList.add("show");
                target.classList.remove("hide");
            } else {
                target.classList.add("hide");
                target.classList.remove("show");
            }
        });
    } else {
        showError();
        camp.innerText = "";
    }
}

function updateAvg(cards) {
    cards.forEach((card) => {
        let temp_id = card.id;
        let originAvg = card.children[2];
        for (let id in avgList) {
            if (id === temp_id) originAvg.innerHTML = avgList[id];
        }
    });
}

function calculateAvg(campList) {
    campList.forEach((camp) => {
        let tempAvg = 0;
        reviews.forEach((review) => {
            if (review["campId"] === camp["id"]) {
                tempAvg += Number(review["avg"]);
            }
        });
        avgList[camp["id"]] = tempAvg;
    });
}

function createAvgList(camps) {
    camps.forEach((camp) => {
        avgList[camp["id"]] = null;
        campList.push(camp);
    });
}

function showError() {
    alert("잘못된 입력입니다!");
    document.querySelector(".home__form--input").value = "";
}

let navbar = document.querySelector("#navbar");
let navbarHeight = navbar.getBoundingClientRect().height;
document.addEventListener("scroll", () => {
    if (window.scrollY > navbarHeight) {
        navbar.classList.add("navbar--dark");
    } else {
        navbar.classList.remove("navbar--dark");
    }
});
