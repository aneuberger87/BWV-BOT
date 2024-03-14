import { excelExists } from "./excel-exists";

export const excelExistsAll = () => {
  const studentsExist = excelExists("studentsList");
  console.log("🚀 ~ excelExistsAll ~ studentsExist:", studentsExist);
  const roomsExist = excelExists("roomsList");
  console.log("🚀 ~ excelExistsAll ~ roomsExist:", roomsExist);
  const companiesExist = excelExists("companiesList");
  console.log("🚀 ~ excelExistsAll ~ companiesExist:", companiesExist);

  return {
    allExist: studentsExist && roomsExist && companiesExist,
    studentsExist,
    roomsExist,
    companiesExist,
  };
};
