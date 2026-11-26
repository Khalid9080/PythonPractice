# সমস্যা ৪: এক লাইনে ডিসকাউন্ট নির্ণয়
# (টপিক: Ternary Operator, Assignment Operators, Operator Precedence)

# সমস্যা: একজন ক্রেতার শপিং কার্টের বর্তমান বিল cart_total = 1200 টাকা এবং তার মেম্বারশিপ স্ট্যাটাস is_member = True।
# যদি বিল ১০০০ টাকার বেশি হয় এবং সে মেম্বার হয়, তবে সে ২০% ডিসকাউন্ট পাবে; অন্যথায় ৫% ডিসকাউন্ট পাবে। Ternary Operator ব্যবহার করে ডিসকাউন্টের পরিমাণ বের করো এবং Assignment Operator (-=) ব্যবহার করে cart_total আপডেট করে প্রিন্ট করো।
# প্রত্যাশিত আউটপুট: Payable Amount: 960.0

# Hints:
# Ternary সিনট্যাক্স: discount = (cart_total * 0.20) if (cart_total > 1000 and is_member) else (cart_total * 0.05)।
# এরপর cart_total -= discount লিখে মূল বিল থেকে ডিসকাউন্ট বাদ দাও।

#---------------------NORMAL WAY-----------------------
cart_total = float(input("Enter your cart total: "))
is_member = True
# Python-এ input() ফাংশন ব্যবহারকারীর কাছ থেকে যা কিছুই নেয়, সেটিকে String (টেক্সট) হিসেবে গ্রহণ করে। input() নেওয়ার পর সেটিকে সংখ্যায় (যেমন float() বা int()) রূপান্তর বা Type Casting করে নিতে হবে।
if (cart_total>1000 and is_member):
    discount_rate = (cart_total*0.2)
else:
    discount_rate = (cart_total*0.05)

cart_total = cart_total - discount_rate

print(f"Your Payable Amount (Discounted): {cart_total:.2f}")


#-----------------TERNARY OPERATOR-------------------------
cart_total = float(input("Enter your cart total 2: "))
is_member = True

discount_rate=(cart_total*0.2) if (cart_total>1000 and is_member) else (cart_total*0.05)
cart_total-=discount_rate
print(f"Your Payable Amount (Discounted): {cart_total:.2f}")