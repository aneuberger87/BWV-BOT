import { PageCompany } from "./page-company";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Firmen",
};

const Page = () => {
  return <PageCompany />;
};

export default Page;

export const revalidate = 0;
export const dynamic = "force-dynamic";
