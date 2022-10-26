SELECT
    st.StaffNo,
    st.Fname,
    st.Lname,
    st.Position,
    st.Sex,
    st.DOB,
    st.Salary,
    st.BranchNo,
    b.Street,
    b.City,
    b.Postcode
FROM
    staff st,
    branch b
WHERE
    st.BranchNo = b.BranchNo;
