function find_camp() {
    let camp = $(".home__form--input").val();
    let boot_name = "";
    let boot_img = "";

    if (!camp) {
        alert("잘못된 입력입니다!");
        location.reload();
        return;
    }

    try {
        for (let i = 0; i < campList.length; i++) {
            if (campList[i]["name"] === camp) {
                boot_name = campList[i]["name"];
                boot_img = campList[i]["boot_img"];
                boot_id = campList[i]["id"];
                break;
            }
        }

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
    } catch (error) {
        alert("잘못된 입력입니다!");
        location.reload();
        return;
    }
}

function updateAvg(cards) {
    cards.forEach(card => {
        let temp_id = card.id;
        let originAvg = card.children[2];
        for (let id in idList) {
            if (id === temp_id) originAvg.innerHTML = idList[id];
        }
    })
}

function calculateAvg(campList) {
    campList.forEach(camp => {
        let tempAvg = 0;
        reviews.forEach(review => {
            if (review['campId'] === camp['id']) {
                tempAvg += Number(review['avg'])
            }
        })
        idList[camp['id']] = tempAvg;
    })
}

function createIdList(camps) {
    camps.forEach(camp => {
        idList[camp['id']] = null;
    });
}

function createCampList(camps) {
    camps.forEach(camp => {
        campList.push(camp);
    });
}