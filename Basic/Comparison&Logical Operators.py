
#--------------COMPARISON OPERATORS-----------------
# অপারেটর	    অর্থ	       উদাহরণ (a = 5, b = 8)	    আউটপুট
# ==	    সমান        (Equal)	a == b	        False
# !=        সমান নয়     (Not Equal) a != b        True
# >         বড়         (Greater than) a > b      False
# <         ছোট        (Less than)a < b          True
# >=        বড় অথবা সমান  a >= 5                   True
# <=        ,োট অথবা সমান b <= 5                   False

#----------------LOGICAL OPERATORS------------------
# একাধিক শর্তকে একসাথে যুক্ত করার জন্য ৩টি লজিক্যাল অপারেটর আছে:
# and: উভয় শর্ত সত্য হলেই কেবল True দেয়।
# or: যেকোনো একটি শর্ত সত্য হলেই True দেয়।
# not: ফলাফল উল্টে দেয় (True থাকলে False করে)।

age=18
has_nid=True

print(age>=18 and has_nid)
print(age<18 or has_nid)
print(not(age<=18))
