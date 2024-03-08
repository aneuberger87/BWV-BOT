"use server";

import { ExcelFileName } from "@/types";
import { excelFileLocation } from "./excel-file-location";
import { existsSync, unlinkSync } from "fs";
import { upload } from "./action-upload";
const URL = process.env.DATAMANAGEMENT_URL!;

export const deleteData = async (type: ExcelFileName) => {
  const path = excelFileLocation(type);
  if (existsSync(path)) {
    unlinkSync(path);
  }
  const response = await fetch(URL + type + "?fileLocation=" + "EMPTY", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: "",
  });
  return { success: true };
};
