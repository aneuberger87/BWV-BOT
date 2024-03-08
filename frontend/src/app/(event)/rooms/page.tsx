import { Metadata } from "next";
import { PageRooms } from "./page-rooms";

export const metadata: Metadata = {
  title: "Räume",
};

const Page = () => {
  return <PageRooms />;
};

export default Page;
