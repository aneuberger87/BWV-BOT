import { ExcelFileName } from "@/types";

export const excelFileName = (type: ExcelFileName) => {
  return type + ".xlsx";
};
