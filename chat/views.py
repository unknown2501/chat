from django.shortcuts import render,HttpResponse
import openai


def chat(request,prompt):
    openai.api_key="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"
    openai.proxy="http://127.0.0.1:7890"
    print(prompt)
    response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'user','content':prompt}
        ]
    )
    msg=response["choices"][0]["message"]["content"]
    print(msg)
    return HttpResponse(msg)
