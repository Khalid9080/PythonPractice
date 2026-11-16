
# প্রশ্ন:
# ধরুন আপনার তৈরি একটি AI মডেলের অ্যাকুরেসি (accuracy) টেস্ট করা হচ্ছে।
# যদি accuracy ৯০ বা তার বেশি হয় (>= 90), তবে প্রিন্ট করবে "Excellent! Ready for Production"।
# যদি accuracy ৭০ বা তার বেশি হয় (>= 70), তবে প্রিন্ট করবে "Good! Needs Minor Tuning"।
# অন্যথায় (else), প্রিন্ট করবে "Poor Accuracy! Train Again"।

accuracy=75.563

if (accuracy >= 90):print("Excellent! Ready for Production")
elif accuracy>=70: print("Good! Needs Minor Tuning")
else : print("Poor Accuracy! Train Again")