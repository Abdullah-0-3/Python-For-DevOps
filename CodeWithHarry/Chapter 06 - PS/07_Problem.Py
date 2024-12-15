post = '''
Hi, I am Harry. I am a software engineer. I am working in a software company. I am a good programmer. I am a good problem solver. I am a good team player. I am a good learner. I am a good listener. I am a good speaker. I am a good writer. I am a good reader. I am a good thinker. I am a good leader. I am a good motivator. I am a good helper. I am a good friend. I am a good human being. I am a good son. I am a good brother. I am a good husband. I am a good father. I am a good citizen.
'''

if ("Harry".lower() in post.lower()):
    print("Post contains Harry")
    post = post.replace("Harry", "Harry Potter")
    print(post)
else:
    print("Harry is not found in the post")