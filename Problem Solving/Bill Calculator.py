# সমস্যা ১: স্মার্ট বিল ও টিপস ক্যালকুলেটর
# (টপিক: Variables, Type Casting, Arithmetic Operators, f-string)
#
# সমস্যা: ধরো, দুটি স্ট্রিং ভেরিয়েবলে একটি রেস্টুরেন্টের খাবারের দাম ও ভ্যাটের হার দেওয়া আছে: food_price = "450.50" এবং vat_percent = "15"।
# তোমাকে এগুলোকে সঠিক সংখ্যায় রূপান্তর করে মোট ভ্যাট এবং ভ্যাটসহ সর্বমোট বিল হিসাব করতে হবে। আউটপুটে দশমিকের পর ঠিক ২ ঘর পর্যন্ত দেখাবে এবং শেষে একটি নতুন লাইনে ধন্যবাদ জানাবে।

# প্রত্যাশিত আউটপুট
#
# Plaintext
# Total Bill (with 15% VAT): 518.08 Taka
# Thank you for dining with us!

food_price="450.50"
vat_percent="15"

food_price=float(food_price)
vat_percent=int(vat_percent)

bill=food_price+(food_price*(vat_percent/100))

print(f"Total bill (with 15% VAT): {bill:.2f} Taka\nThank you for dining with us!")
