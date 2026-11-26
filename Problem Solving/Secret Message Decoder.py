# সমস্যা ৫: গোপন কোড ডিকোডার (Secret Message Decoder)
# (টপিক: String Slicing, String Methods, Escape Characters)
# সমস্যা: নিচের এলোমেলো স্ট্রিংটি থেকে আসল বার্তাটি বের করো:
# secret = "xxP#y#t#h#o#n# #i#s# #F#u#n!yy"

# প্রত্যাশিত আউটপুট: Python is Fun!

# Hints:
# শুরুতে "xx" (২টি অক্ষর) এবং শেষে "yy" (২টি অক্ষর) আছে। স্লাইসিং secret[2:-2] ব্যবহার করে এগুলো বাদ দাও।
# এরপর .replace("#", "") মেথড ব্যবহার করে মাঝের সব # চিহ্ন মুছে ফেলো।

secret = "xxP#y#t#h#o#n# #i#s# #F#u#n!yy"
pass_decoder=secret[2:-2].replace("#","")
print(pass_decoder)