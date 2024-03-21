"use server";

import { postRoomUpdateForEvent } from "@/lib/fetches";

export const actionRewireRoom = async (
  companyId: string,
  roomId: string,
  timeSlot: string,
) => {
  const response = await postRoomUpdateForEvent(
    companyId,
    roomId,
    timeSlot as "A" | "B" | "C" | "D" | "E",
  );
  return response;
};
