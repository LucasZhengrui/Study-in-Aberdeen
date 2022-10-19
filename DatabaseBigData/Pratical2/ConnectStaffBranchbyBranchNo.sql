SELECT Staff.Fname, Staff.Lname, Staff.Position, Branch.Street, Branch.City, Branch.BranchNo
FROM Staff, Branch
WHERE Staff.BranchNo = Branch.BranchNo;
