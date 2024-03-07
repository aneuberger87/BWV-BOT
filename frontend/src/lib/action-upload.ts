"use server";

import { ExcelFileName } from "@/types";
import { writeFile } from "fs/promises";
import { join } from "path";
import { excelFileName } from "./excel-file-name";
import { excelFileLocation } from "./excel-file-location";

const URL = process.env.DATAMANAGEMENT_URL!;
const FOLDER = process.env.FOLDER_SHARE!;

export const upload = async (data: {
  type: ExcelFileName | "EMPTY";
  fileBase64: string;
}) => {
  // Decode the Base64 string to binary data
  const matches = data.fileBase64.match(/^data:(.+);base64,(.*)$/);
  if (!matches || matches.length !== 3) {
    return { success: false, error: "Invalid Base64 string" };
  }

  const mimeType = matches[1];
  const base64Data = matches[2];
  const buffer = Buffer.from(base64Data, "base64");

  const filePath =
    data.type !== "EMPTY" ? excelFileLocation(data.type) : "EMPTY";

  try {
    await writeFile(filePath, buffer);
    const response = await fetch(URL + "?fileLocation=" + filePath, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: "",
    });
    if (!response.ok) {
      console.log("🚀 ~ response:", response);
      console.error("Error uploading file:", response.statusText);
      return { success: false, error: "Error uploading file" };
    }
    return { success: true, filePath: filePath };
  } catch (error) {
    console.error("Error saving file:", error);
    return { success: false, error: "Error saving file" };
  }
};
