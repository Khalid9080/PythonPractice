# পাসওয়ার্ড সিকিউরিটি চেকার
# (টপিক: Booleans, Comparison Operators, Logical Operators, Membership Operators)

# সমস্যা: একটি পাসওয়ার্ড password = "Dhaka@2026" শক্তিশালী কি না তা যাচাই করো। পাসওয়ার্ডটি শক্তিশালী (True) হবে যদি নিচের সবগুলো শর্ত পূরণ করে:
# পাসওয়ার্ডের দৈর্ঘ্য কমপক্ষে ৮ অক্ষরের হতে হবে।
# পাসওয়ার্ডের ভেতরে "@" অথবা "#" চিহ্ন থাকতে হবে।
# পাসওয়ার্ডের ভেতরে "123" থাকা যাবে না।
# প্রত্যাশিত আউটপুট: Is Password Strong: True

# Hints:
# দৈর্ঘ্য মাপার জন্য len(password) >= 8 ব্যবহার করো।
# চিহ্ন যাচাই করতে ("@" in password or "#" in password) লেখো (বন্ধনী দেওয়া জরুরি—Operator Precedence মনে রেখো!)।
# "123" নেই তা নিশ্চিত করতে "123" not in password লিখে সবগুলোকে and দিয়ে যুক্ত করো।

password="Dhaka@2026"
pass_test1=len(password)>=8 and ("@" in password or "#" in password) and "123" not in password
print("Is Password Strong:",pass_test1)

