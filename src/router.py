def route_question(question):

    question = question.lower()


    if any(
        word in question
        for word in [
            "medicine",
            "drug",
            "tablet",
            "treatment"
        ]
    ):

        return "drug"


    elif any(
        word in question
        for word in [
            "symptom",
            "sign",
            "feel"
        ]
    ):

        return "symptom"



    elif any(
        word in question
        for word in [
            "who",
            "guideline",
            "recommend"
        ]
    ):

        return "who"



    else:

        return "medical" 