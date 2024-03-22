"use server";

import { postAddRooms } from "@/lib/fetches";
import { RoomList } from "@/types";

export const addRoomAction = async (data: {
  roomNumber: string;
  roomCapacity: string;
}) => {
  const listToAdd: RoomList = {
    roomList: [
      {
        roomId: data.roomNumber,
        capacity: Number(data.roomCapacity),
      },
    ],
  };

  const result = await postAddRooms(listToAdd);

  return {
    success: true,
  };
};
