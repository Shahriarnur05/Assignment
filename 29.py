
def time(s_h,s_s,e_h,e_s):
    s_time = s_h * 60 + s_s
    e_time = e_h * 60 + e_s

    main = e_time - s_time 
    m_h = main // 60
    m_s = main - m_h * 60
    return m_h,m_s

s_h , s_s = [int (s_h) for s_h in input("Enter starting time: ").split(":")]
e_h , e_s = [int (e_h) for e_h in input("Enter starting time: ").split(":")]

m_h,m_s = time(s_h,s_s,e_h,e_s)
print(f"Elapsed Time is  {m_h} hours and {m_s} minutes.")


