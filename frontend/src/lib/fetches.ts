import { CompanyList, RoomList, StudentList } from "../types";

const BASE_URL = process.env.DATAMANAGEMENT_URL as string;

export const getAllRooms = async () => {
  try {
    const response = await fetch(`${BASE_URL}rooms`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return (await response.json()) as RoomList;
  } catch (error) {
    console.error("getAllCompanies error: ", error);
    throw error;
  }
};

export const getAllCompanies = async () => {
  try {
    const response = await fetch(`${BASE_URL}companies`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return (await response.json()) as CompanyList;
  } catch (error) {
    console.error("getAllCompanies error: ", error);
    throw error;
  }
};

export const getAllStudents = async () => {
  try {
    const response = await fetch(`${BASE_URL}students`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return (await response.json()) as StudentList;
  } catch (error) {
    console.error("getAllStudents error: ", error);
    throw error;
  }
};

export const postStudentWishes = async (studentsWithWishes: any /*TODO */) => {
  try {
    const response = await fetch(`${BASE_URL}students/wishes`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(studentsWithWishes),
    });
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  } catch (error) {
    console.error("postStudentWishes error: ", error);
    throw error;
  }
};

export const getAllDummyStudents = async () => {
  try {
    const response = await fetch(`${BASE_URL}students/dummies`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("getAllDummyStudents error: ", error);
    throw error;
  }
};

export const getAllDummyStudentsWithWishes = async () => {
  try {
    const response = await fetch(`${BASE_URL}students/wishes/dummies`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return (await response.json()) as StudentList;
  } catch (error) {
    console.error("getAllDummyStudentsWithWishes error: ", error);
    throw error;
  }
};

export const getAllDummyCompaniesWithRoomsAndTimeslots = async () => {
  try {
    const response = await fetch(`${BASE_URL}companies/room/dummy`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return (await response.json()) as CompanyList;
  } catch (error) {
    console.error("getAllDummyCompaniesWithRoomsAndTimeslots error: ", error);
    throw error;
  }
};

export const getAllDummyCompanies = async () => {
  try {
    const response = await fetch(`${BASE_URL}companies/dummy`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("getAllDummyCompanies error: ", error);
    throw error;
  }
};

export const webhookCalculate = async () => {
  try {
    const response = await fetch(`${BASE_URL}calculate`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  } catch (error) {
    console.error("webhookCalculate error: ", error);
    throw error;
  }
};
