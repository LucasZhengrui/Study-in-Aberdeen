SELECT
    st.StaffNo,
    st.BranchNo,
    st.Fname,
    st.Lname,
    st.Position,
    st.Sex,
    st.DOB,
    st.Salary,
    b.Street,
    b.City,
    b.Postcode,
    c.ClientNo,
    c.Fname,
    c.Lname,
    c.TelNo,
    c.PrefType,
    c.MaxRent,
    pp.PropertyNo,
    pp.Postcode,
    pp.Type,
    pvo.OwnerNo,
    pvo.Fname,
    pvo.Lname,
    pvo.Address,
    pvo.TelNo,
    r.ClientNo,
    r.DateJoined
FROM
    staff st,
    branch b,
    CLIENT c,
    privateowner pvo,
    propertyforrent pp,
    registration r
WHERE
    st.BranchNo = b.BranchNo AND
    b.BranchNo = pp.BranchNo AND
    pp.BranchNo = st.BranchNo AND
    st.StaffNo = pp.StaffNo AND
    c.ClientNo = r.ClientNo AND
    pvo.OwnerNo = pp.OwnerNo AND
    r.BranchNo = b.BranchNo AND
    pp.BranchNo = r.BranchNo AND
    pp.BranchNo = st.BranchNo AND
    r.BranchNo = st.BranchNo AND
    r.StaffNo = st.StaffNo;
