import { cache } from "react";
import "server-only";
import { excelExists } from "./excel-exists";
import { getFrontendData } from "./frontend-data";

export const getDataStatus = () => {
  const studentsExist = excelExists("studentsList");
  const roomsExist = excelExists("roomsList");
  const companiesExist = excelExists("companiesList");
  const frontendData = getFrontendData();

  return {
    input: {
      excel: {
        allExist: studentsExist && roomsExist && companiesExist,
        studentsExist,
        roomsExist,
        companiesExist,
      },
    },
    output: frontendData,
  };
};

export const getDataStatusCachable = cache(getDataStatus);
