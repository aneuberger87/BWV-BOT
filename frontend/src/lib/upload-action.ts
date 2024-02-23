"use server";

import { writeFile } from "fs/promises";
import { tmpdir } from "os";
import { join } from "path";

export const upload = async (fileBase64: string) => {
  // Decode the Base64 string to binary data
  const matches = fileBase64.match(/^data:(.+);base64,(.*)$/);
  if (!matches || matches.length !== 3) {
    return { success: false, error: "Invalid Base64 string" };
  }

  const mimeType = matches[1];
  const base64Data = matches[2];
  const buffer = Buffer.from(base64Data, "base64");

  // Generate a file path
  const tempFilePath = join(tmpdir(), `upload_${Date.now()}`);
  try {
    // Write the binary data to a file in the temp directory
    await writeFile(tempFilePath, buffer);

    console.log(`File saved to ${tempFilePath}`);

    // At this point, you have the file saved at tempFilePath, and you can process it as needed

    return { success: true, filePath: tempFilePath };
  } catch (error) {
    console.error("Error saving file:", error);
    return { success: false, error: "Error saving file" };
  }
};
