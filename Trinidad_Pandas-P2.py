 "source": [
    "#### PROBLEM 2\n",
    "\n",
    "<span style=\"color:green\">Objective:</span>\n",
    "\n",
    "1. Perform subsetting, slicing, and indexing operations on the cars DataFrame to extract specific data."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c899a01b-56a3-48c9-bf1c-604f46d70b70",
   "metadata": {},
   "source": [
    "<span style=\"color:green; font-size:16px; font-weight:bold\">A. Display the first five rows with odd-numbered columns of the cars DataFrame.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "5a3139cc-d8b9-48fe-8dff-40090d2e656b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.875</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>21.4</td>\n",
       "      <td>6</td>\n",
       "      <td>258.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.08</td>\n",
       "      <td>3.215</td>\n",
       "      <td>19.44</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Valiant</td>\n",
       "      <td>18.1</td>\n",
       "      <td>6</td>\n",
       "      <td>225.0</td>\n",
       "      <td>105</td>\n",
       "      <td>2.76</td>\n",
       "      <td>3.460</td>\n",
       "      <td>20.22</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Merc 240D</td>\n",
       "      <td>24.4</td>\n",
       "      <td>4</td>\n",
       "      <td>146.7</td>\n",
       "      <td>62</td>\n",
       "      <td>3.69</td>\n",
       "      <td>3.190</td>\n",
       "      <td>20.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Merc 280</td>\n",
       "      <td>19.2</td>\n",
       "      <td>6</td>\n",
       "      <td>167.6</td>\n",
       "      <td>123</td>\n",
       "      <td>3.92</td>\n",
       "      <td>3.440</td>\n",
       "      <td>18.30</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
       "1   Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
       "3  Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
       "5         Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0     3   \n",
       "7       Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0     4   \n",
       "9        Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0     4   \n",
       "\n",
       "   carb  \n",
       "1     4  \n",
       "3     1  \n",
       "5     1  \n",
       "7     2  \n",
       "9     4  "
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Extracting rows with odd-numbered indices using slicing and indexing.\n",
    "# Display starting from index 1 and limit the result to the first five rows.\n",
    "first_five_odd = cars_file.iloc[1::2].head(5)\n",
    "first_five_odd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57a42b1b-1e83-4739-993a-fa84e1dc9a41",
   "metadata": {},
   "source": [
    "<span style=\"color:green; font-size:16px; font-weight:bold\">B. Display the Row that Contains the Model 'Mazda RX4'.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "d98497dc-a457-4f77-af11-8a92b85ed9ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.9</td>\n",
       "      <td>2.62</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
       "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Indexing to get rows where 'Model' is 'Mazda RX4'\n",
    "cars_file.loc[(cars_file['Model']=='Mazda RX4')]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b3801330-9dd6-4a0d-9ba0-fbc890250d65",
   "metadata": {},
   "source": [
    "<span style=\"color:green; font-size:16px; font-weight:bold\">C. Determine the Number of Cylinders for the Car Model 'Camaro Z28'.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "b3ba0d54-6f9f-4d6b-a89e-ef3422c7252d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Camaro Z28</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Model  cyl\n",
       "23  Camaro Z28    8"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Filter the DataFrame to include only rows where the 'Model' is 'Camaro Z28'\n",
    "# Display only the 'Model' and 'cyl' columns\n",
    "cars_file.loc[cars_file['Model']=='Camaro Z28', ['Model', 'cyl'] ]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a15257b-4c98-4ae2-a2c9-ed2fe12d3b63",
   "metadata": {},
   "source": [
    "<span style=\"color:green; font-size:16px; font-weight:bold\">D. Determine the Number of Cylinders and Gear Type for Car Models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.</span>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "bae76d56-440c-403a-8073-41c874319f4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Honda Civic</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Model  cyl  gear\n",
       "1    Mazda RX4 Wag    6     4\n",
       "18     Honda Civic    4     4\n",
       "28  Ford Pantera L    8     5"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Filter the DataFrame to include rows for specific car models: 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.\n",
    "# The `isin` method is used to check if the 'Model' column values are in the specified list of car models.\n",
    "# Display the 'Model', 'cyl', and 'gear' columns for these selected car models.\n",
    "filtered_df = cars_file.loc[cars_file['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']]\n",
    "filtered_df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2137015-5bd4-44a5-b20d-f84371aa2345",
   "metadata": {},
   "source": [
    "<span style= \"color:red; font-weight:bold\">Note:</span> \n",
    "Pandas is case-sensitive when comparing strings. This means that the strings you provide must match exactly, including the capitalization, in order for the comparison to work correctly. For example, 'Mazda' is not the same as 'mazda', and attempting to filter with one when the data contains the other will not return a match."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "798268ba-4341-4cb4-94ba-34a1fabaed30",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
