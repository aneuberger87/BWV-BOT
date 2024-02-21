import { CompanyList, Student, StudentList } from "../types";

const BASE_URL = "http://localhost:8080/"; //TODO Replace with your actual base URL

export const getAllCompanies = async () => {
  try {
    const response = await fetch(`${BASE_URL}companies`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return (await response.json()) as CompanyList;
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
    throw error;
  }
};

export const getAllStudents = async () => {
  try {
    const response = await fetch(`${BASE_URL}students`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
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
    console.error("There was a problem with the fetch operation:", error);
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
    console.error("There was a problem with the fetch operation:", error);
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
    console.error("There was a problem with the fetch operation:", error);
    throw error;
  }
};

export const getAllDummyCompaniesWithRoomsAndTimeslots = async () => {
  try {
    const response = await fetch(`${BASE_URL}companies/room/dummy`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
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
    console.error("There was a problem with the fetch operation:", error);
    throw error;
  }
};
