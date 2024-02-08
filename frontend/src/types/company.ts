export type company = {
  id: number;
  compName: string;
  trainingOccupation: string;
  meeting: {
    timeSlot: string;
    room: string;
  }[];
};

export type Unternehmensliste = company[];
