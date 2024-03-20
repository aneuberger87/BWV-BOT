"use server";

import { setFrontendData } from "./frontend-data";

export const dataReset = async () => {
  // TODO remove this timeout
  await new Promise((resolve) => setTimeout(resolve, 2000));

  setFrontendData({
    calculated: false,
    downloaded: {
      students: false,
      rooms: false,
      companies: false,
    },
  });
  return { success: true };
};
