function find_camp() {
    let camp = $(".home__form--input").val();
    if (camp == "") {
        alert("잘못된 입력입니다!");
        return;
    }

    let boot_name = "";
    let boot_img = "";
    for (let i = 0; i < campList.length; i++) {
        if (campList[i]["name"] == camp) {
            boot_name = campList[i]["name"];
            boot_img = campList[i]["boot_img"];
            boot_id = campList[i]["id"];
            break;
        }
    }

    let targetList = document.querySelectorAll(".card");
    targetList.forEach((target) => {
        target_id = target.attributes[2].nodeValue;
        if (target_id === boot_id) {
            target.classList.add("show");
            target.classList.remove("hide");
        } else {
            target.classList.add("hide");
            target.classList.remove("show");
        }
    });
}