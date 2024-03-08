import { ExcelFileName } from "@/types";

const FOLDER = process.env.FOLDER_SHARE!;

export const excelFileLocation = (type: ExcelFileName) => {
  return FOLDER + type + ".xlsx";
};
