let currentTask = "qa";


const taskButtons =
    document.querySelectorAll(".task-button");


const mainInput =
    document.getElementById("main-input");


const inputLabel =
    document.getElementById("input-label");


const levelContainer =
    document.getElementById("level-container");


const countContainer =
    document.getElementById("count-container");


const goalContainer =
    document.getElementById("goal-container");


const goalInput =
    document.getElementById("goal");


const questionCount =
    document.getElementById("question-count");


const level =
    document.getElementById("level");


const submitButton =
    document.getElementById("submit-button");


const statusBox =
    document.getElementById("status");


const resultCard =
    document.getElementById("result-card");


const resultTitle =
    document.getElementById("result-title");


const resultContent =
    document.getElementById("result-content");



const taskConfig = {

    qa: {
        label: "Your question",
        placeholder:
            "Example: What is object-oriented programming?",
        title: "Answer"
    },

    explain: {
        label: "Topic to explain",
        placeholder:
            "Example: Explain inheritance in Java",
        title: "Explanation"
    },

    quiz: {
        label: "Quiz topic",
        placeholder:
            "Example: Python loops",
        title: "Generated Quiz"
    },

    summarize: {
        label: "Text to summarize",
        placeholder:
            "Paste your study material here...",
        title: "Summary"
    },

    recommend: {
        label: "Topic you want to learn",
        placeholder:
            "Example: Data Science",
        title: "Personalized Learning Path"
    }

};



taskButtons.forEach(button => {

    button.addEventListener(
        "click",
        () => {

            taskButtons.forEach(
                item =>
                    item.classList.remove("active")
            );

            button.classList.add("active");

            currentTask =
                button.dataset.task;

            updateForm();

            clearResult();
        }
    );

});



function updateForm() {

    const config =
        taskConfig[currentTask];


    inputLabel.textContent =
        config.label;


    mainInput.placeholder =
        config.placeholder;


    countContainer.style.display =
        currentTask === "quiz"
            ? "block"
            : "none";


    goalContainer.style.display =
        currentTask === "recommend"
            ? "block"
            : "none";


    if (currentTask === "summarize") {

        levelContainer.style.display =
            "block";

    } else {

        levelContainer.style.display =
            "block";
    }


    submitButton.textContent =
        currentTask === "qa"
            ? "💬 Ask EduGenie"
            : currentTask === "explain"
                ? "💡 Explain Topic"
                : currentTask === "quiz"
                    ? "📝 Generate Quiz"
                    : currentTask === "summarize"
                        ? "📚 Summarize"
                        : "🧭 Create Learning Path";
}



function showStatus(
    message,
    isError = false
) {

    statusBox.textContent =
        message;

    statusBox.style.display =
        "block";


    if (isError) {

        statusBox.classList.add(
            "error"
        );

    } else {

        statusBox.classList.remove(
            "error"
        );
    }
}



function hideStatus() {

    statusBox.style.display =
        "none";
}



function clearResult() {

    resultCard.style.display =
        "none";

    resultContent.innerHTML =
        "";
}



function escapeHtml(value) {

    return String(value)

        .replaceAll("&", "&amp;")

        .replaceAll("<", "&lt;")

        .replaceAll(">", "&gt;")

        .replaceAll('"', "&quot;")

        .replaceAll("'", "&#039;");
}



submitButton.addEventListener(
    "click",
    async () => {

        const input =
            mainInput.value.trim();


        if (!input) {

            showStatus(
                "Please enter something first.",
                true
            );

            return;
        }


        if (
            currentTask === "recommend" &&
            !goalInput.value.trim()
        ) {

            showStatus(
                "Please enter your learning goal.",
                true
            );

            return;
        }


        submitButton.disabled =
            true;


        showStatus(
            "EduGenie is thinking..."
        );


        clearResult();


        try {

            let endpoint;

            let body;


            if (currentTask === "qa") {

                endpoint = "/qa";

                body = {
                    question: input,
                    level: level.value
                };

            }


            else if (
                currentTask === "explain"
            ) {

                endpoint = "/explain";

                body = {
                    topic: input,
                    level: level.value
                };

            }


            else if (
                currentTask === "quiz"
            ) {

                endpoint = "/quiz";

                body = {
                    topic: input,
                    number_of_questions:
                        Number(
                            questionCount.value
                        ),
                    level: level.value
                };

            }


            else if (
                currentTask === "summarize"
            ) {

                endpoint = "/summarize";

                body = {
                    text: input,
                    level: level.value
                };

            }


            else if (
                currentTask === "recommend"
            ) {

                endpoint =
                    "/learn/recommendations";

                body = {
                    topic: input,
                    goal:
                        goalInput.value.trim(),
                    level: level.value
                };
            }


            const response =
                await fetch(
                    endpoint,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(body)
                    }
                );


            const data =
                await response.json();


            if (!response.ok) {

                throw new Error(
                    data.detail ||
                    "Something went wrong."
                );
            }


            if (!data.success) {

                throw new Error(
                    data.error ||
                    "AI request failed."
                );
            }


            hideStatus();

            resultCard.style.display =
                "block";


            resultTitle.textContent =
                taskConfig[currentTask].title;


            if (currentTask === "quiz") {

                renderQuiz(
                    data.quiz
                );

            } else {

                resultContent.textContent =
                    data.answer ||
                    data.explanation ||
                    data.summary ||
                    data.recommendations ||
                    "No result returned.";
            }


            resultCard.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });


        } catch (error) {

            showStatus(
                error.message,
                true
            );

        } finally {

            submitButton.disabled =
                false;
        }

    }
);



function renderQuiz(quiz) {

    if (
        !quiz ||
        !Array.isArray(quiz.questions)
    ) {

        throw new Error(
            "Invalid quiz received."
        );
    }


    resultContent.innerHTML = "";


    quiz.questions.forEach(
        (item, index) => {

            const question =
                document.createElement(
                    "div"
                );


            question.className =
                "quiz-question";


            const title =
                document.createElement(
                    "h3"
                );


            title.textContent =
                `${index + 1}. ${item.question}`;


            question.appendChild(
                title
            );


            const options =
                document.createElement(
                    "div"
                );


            options.className =
                "quiz-options";


            item.options.forEach(
                option => {

                    const optionElement =
                        document.createElement(
                            "div"
                        );


                    optionElement.className =
                        "quiz-option";


                    optionElement.textContent =
                        option;


                    options.appendChild(
                        optionElement
                    );
                }
            );


            question.appendChild(
                options
            );


            const answer =
                document.createElement(
                    "div"
                );


            answer.className =
                "quiz-answer";


            answer.innerHTML =
                `<strong>Answer:</strong>
                 ${escapeHtml(item.answer)}
                 <br><br>
                 <strong>Explanation:</strong>
                 ${escapeHtml(item.explanation)}`;


            question.appendChild(
                answer
            );


            resultContent.appendChild(
                question
            );
        }
    );
}



updateForm();
