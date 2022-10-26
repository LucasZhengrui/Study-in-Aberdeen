SELECT
    st.StaffNo,
    st.Fname,
    st.Lname,
    b.Street,
    b.City,
    b.Postcode,
    b.BranchNo,
    pp.Type
FROM
    staff st,
    propertyforrent pp,
    branch b
WHERE
    st.BranchNo = b.BranchNo AND pp.BranchNo = st.BranchNo AND st.StaffNo = pp.StaffNo;
