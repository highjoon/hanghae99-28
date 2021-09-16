function clickEvent(elementList) {
    elementList.forEach((element) => {
        element.addEventListener("click", (event) => {
            let score = Number(event.target.innerText);
            let target = event.target.previousSibling.parentNode.id;
            getRadioReview(score, target);
        });
    });
}

function getRadioReview(score, target) {
    reviewList[target] = score;
}

function getCommentReview() {
    let commentList = commentBox.value.split("\n");
    commentList.forEach((com) => {
        reviewList["comment"] = com;
    });
}

function seperateReviewList(reviewList) {
    overall = reviewList["overall"];
    period = reviewList["period"];
    recommend = reviewList["recommend"];
    tuition = reviewList["tuition"];
    comment = reviewList["comment"];
    avg = (Number(overall) + Number(period) + Number(recommend) + Number(tuition)) / 4;
}
