# সমস্যা ২: ইউজারনেম জেনারেটর (Username Generator)
# (টপিক: Strings, Slicing, Modify Strings, Concatenate)
#
# সমস্যা: একজন ব্যবহারকারীর পুরো নাম এবং জন্মসাল দেওয়া আছে:
# full_name = "  tanvir ahmed  " এবং birth_year = 2002।
# তোমাকে নামটির দুই পাশের বাড়তি স্পেস মুছে, নামের প্রথম ৩টি অক্ষর এবং শেষের ২টি অক্ষর ছোট হাতের অক্ষরে নিয়ে তার সাথে জন্মসালের শেষ ২টি অঙ্ক যুক্ত করে একটি ইউজারনেম তৈরি করতে হবে।

# প্রত্যাশিত আউটপুট: taned02
#
# Hints:
#
# প্রথমে .strip().lower() ব্যবহার করে নামের বাড়তি স্পেস সরাও এবং সব ছোট হাতের করো (এখন নাম হবে "tanvir ahmed"—মাঝের স্পেস বাদ দিতে চাইলে .replace(" ", "") ব্যবহার করতে পারো)।
#
# স্লাইসিং [0:3] দিয়ে প্রথম ৩টি অক্ষর এবং [-2:] দিয়ে শেষ ২টি অক্ষর নাও।
#
# birth_year-কে str() দিয়ে স্ট্রিং বানিয়ে শেষ ২ অঙ্ক [-2:] স্লাইস করে + দিয়ে জোড়া লাগাও।


full_name="    osman goni    "
birth_year=1968

halfdone_name=full_name.strip().lower()
semihalfdone_name=halfdone_name[0:3]
semihalfdone_name2=halfdone_name[-2:]
year=str(birth_year)[-2:]
# Python-এ সংখ্যার ওপর সরাসরি স্লাইসিং ([2:4]) করা যায় না—এতে TypeError: 'int' object is not subscriptable এরর দেখাবে।
# সমাধান: স্লাইস করার আগে str(birth_year) দিয়ে সংখ্যাটিকে স্ট্রিংয়ে রূপান্তর করে নিতে হবে, তারপর [2:4] বা [-2:] দিতে হবে।
final_username=semihalfdone_name+semihalfdone_name2+year

print(final_username)