"use server";

export const addRoomAction = async (data: {
  roomNumber: string;
  roomCapacity: string;
}) => {
  return {
    success: true,
  };
};
