export type Meeting = {
  timeSlot: string;
  room: string | null;
};

export type Company = {
  id: number;
  compName: string;
  trainingOccupation: string;
  meeting: Meeting[];
  numberOfMembers: number;
};

export type CompanyList = {
  company: Company[];
};

export type Wish = {
  compId: number;
  timeSlot: string;
};

export type Student = {
  prename: string;
  surname: string;
  schoolClass: string;
  wishList: Wish[];
};

// TODO Seperate normal list from resultlist
export type StudentList = {
  student: Student[];
};
