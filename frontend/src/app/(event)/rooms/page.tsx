import { Metadata } from "next";
import { PageRooms } from "./page-rooms";

export const metadata: Metadata = {
  title: "Räume",
};

const Page = () => {
  return <PageRooms />;
};

export default Page;

export const revalidate = 0;
export const dynamic = "force-dynamic";
