#include <iostream>

#include <fstream>

#include <string>
#include <algorithm>

using namespace std;

bool
is_digit (int num)
{
  return num >= 48 && num <= 57;
}

string nums[9] = {
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine"
};

int
main ()
{
  string l;
  ifstream f ("data");
  int fd = -1;
  int sd = -1;
  int sum = 0;
  int c = 0;
  while (getline (f, l))
    {
      c++;
      int fd = -1;
      int sd = -1;
      int fdix = -1;
      int sdix = -1;
      int ll = l.length ();
      for (int i = 0; i < ll; i++)
	{
	  if (fd == -1)
	    {
	      if (is_digit (l[i]))
		{
		  fd = l[i];
		  fdix = i;
		}
	    }
	  if (sd == -1)
	    {
	      if (is_digit (l[ll - i - 1]))
		{
		  sd = l[ll - i - 1];
		  sdix = ll - i - 1;
		}
	    }
	}



      int num = -1;
      int numidx = 1000;
      for (int x = 0; x < 9; x++)
	{
	  int ix = l.find (nums[x]);
	  if (ix != -1)
	    {
	      if (ix < numidx)
		{
		  num = x;
		  numidx = ix;
		}
	    }
	}
      if (numidx < fdix || fdix == -1)
	{
	  if (numidx != 1000)
	    {
	      fd = num + 49;

	    }
	}


      num = -1;
      numidx = 1000;
      reverse (l.begin (), l.end ());
      cout << "l" << l << " ";
      for (int x = 0; x < 9; x++)
	{
	  reverse (nums[x].begin (), nums[x].end ());

	  int ix = l.find (nums[x]);
	  reverse (nums[x].begin (), nums[x].end ());
	  if (ix != -1)
	    {
	      cout << "num:" << nums[x] << " ";
	      if (ix < numidx)
		{
		  num = x;
		  numidx = ix;
		}
	    }


	}
      cout << "numidx:sdix:" << numidx << " " << sdix << " ";

      if (ll - numidx > sdix || sdix == -1)
	{
	  if (numidx != 1000)
	    {

	      sd = num + 49;

	    }
	}
      if (c > 0)
	{
	  cout << "fd" << fd;
	  cout << "sd:" << sd << "\n";
	}
      sum += ((fd - 48) * 10) + sd - 48;
    }




  f.close ();
  cout << "sum:" << sum;
  return 0;
}